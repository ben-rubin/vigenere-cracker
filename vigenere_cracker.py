# Assumptions:
# 1. cypher text is hex string as ascii bytes (2 cypher text characters == 1 hex cypher text nibble)
# 2. key length is between 2 and 30
# 3. plain text is ascii characters between 32 and 127 in decimal
from collections import defaultdict
import random
chunk = 2


def get_pseudo_random_hex_key(key_len: int) -> str:
    return ''.join([int_to_hex_str(k) for k in [random.randint(1, 255) for i in range(1, key_len + 1)]])


def ascii_string_to_hex_array(ascii_text: str) -> list:
    return [int_to_hex_str(ord(t)) for t in ascii_text]


# - convert int to a 2 byte hex string
# - strip 0x and pad with zeros to 2 bytes
def int_to_hex_str(num: int) -> str:
    return '{0:0{1}x}'.format(num, 2)


# Encrypt plain text into a sting of hex nibbles using xor
# i.e encrypt('a', 'a') will output '00'
def encrypt(plain_text: str, hex_key: str) -> str:
    hex_key_arr = [hex_key[i:i + chunk] for i in range(0, len(hex_key), chunk)]
    key_len = len(hex_key_arr)
    plain_text = list(plain_text)
    cypher_hex_str = ''
    for idx, pt in enumerate(plain_text):
        cypher_hex_str += int_to_hex_str(ord(pt) ^ int(hex_key_arr[idx % key_len], 16))

    return cypher_hex_str


def decrypt(cypher: str, hex_key: str) -> str:
    plain_text = ''
    key_array = [hex_key[i:i + chunk] for i in range(0, len(hex_key), chunk)]
    key_array_len = len(key_array)
    cypher_array = [cypher[i:i + chunk] for i in range(0, len(cypher), chunk)]
    for idx, c in enumerate(cypher_array):
        plain_text += chr(int(c, 16) ^ int(key_array[idx % key_array_len], 16))

    return plain_text


def get_streams_for_key_len(cypher_array: list, key_len: int) -> dict:
    return dict(zip([i for i in range(0, key_len)], [cypher_array[i::key_len] for i in range(0, key_len)]))


# calculate index of coincidence for a single stream
def get_stream_ic(stream: list) -> int:
    stream_length = len(stream)
    return sum([(stream.count(c) / stream_length) ** 2 for c in set(stream)])


# calculate average index of coincidence for streams
def get_average_stream_ic(streams: dict) -> float:
    totals = defaultdict()
    for sIdx, stream in streams.items():
        totals[sIdx] = get_stream_ic(stream)

    return sum([val for v, val in totals.items()]) / len(totals)


def get_cypher_array(cypher) -> list:
    return [cypher[i:i + chunk] for i in range(0, len(cypher), chunk)]


def find_key_len_candidates(cypher: str) -> defaultdict:
    cypher_array = get_cypher_array(cypher)
    candidates = defaultdict()
    totals = defaultdict()

    for key_len in range(2, 30):
        candidates[key_len] = get_streams_for_key_len(cypher_array, key_len)
        totals[key_len] = get_average_stream_ic(candidates[key_len])

    return totals


def find_key(cypher: str, key_len: int) -> str:
    english_letters_decimal = [*range(65, 91), *range(97, 123)]
    decrypted_streams = defaultdict(dict)
    candidate_totals = defaultdict(dict)
    letter_frequencies = [8.497, 1.492, 2.202, 4.253, 11.162, 2.228, 2.015, 6.094, 7.546, 0.153, 1.292, 4.025, 2.406,
                          6.749, 7.507, 1.929, 0.095, 7.587, 6.327, 9.356, 2.758, 0.978, 2.560, 0.150, 1.994, 0.077]
    letter_frequencies_map = dict(zip([chr(a) for a in range(97, 123)], letter_frequencies))

    streams = get_streams_for_key_len(get_cypher_array(cypher), key_len)
    for key_chr_idx, stream in enumerate(streams.values(), 1):
        for n in range(1, 255):
            decrypted = [int(c, 16) ^ n for c in stream]

            # candidate is valid if all decrypted values are printable characters
            if max(decrypted) < 127 and min(decrypted) >= 32:
                # candidates for key (n). convert to lowercase
                candidate = [chr(d).lower() for d in decrypted if d in english_letters_decimal]
                if len(candidate):
                    decrypted_streams[key_chr_idx][n] = candidate

        # calculate sum of differences between candidate stream letter frequencies and known english language frequencies
        # we do this to find candidate that is closest to known english language letter frequencies
        for c_idx, decrypted_stream in decrypted_streams[key_chr_idx].items():
            c_unique = list(set(decrypted_stream))
            key_chr_total = sum(
                [abs(letter_frequencies_map[letter] / 100 - decrypted_stream.count(letter) / len(decrypted_stream)) for letter in c_unique])
            candidate_totals[key_chr_idx][c_idx] = key_chr_total

    probable_key = ''
    for idx, candidate_total in candidate_totals.items():
        probable_key += int_to_hex_str([k for k, v in candidate_total.items() if v == min(candidate_total.values())][0])

    return probable_key

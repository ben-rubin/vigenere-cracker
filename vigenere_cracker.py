# Assumptions:
# 1. cypher text is hex string as ascii bytes (2 cypher text characters == 1 hex cypher text nibble)
from collections import defaultdict


def ascii_string_to_hex_array(ascii_text):
    return [int_to_hex_str(ord(t)) for t in ascii_text]


# - convert int to a 2 byte hex string
# - strip 0x and pad with zeros to 2 bytes
def int_to_hex_str(num):
    return '{0:0{1}x}'.format(num, 2)


# Encrypt plain text into a sting of hex nibbles using xor
# i.e encrypt('a', 'a') will output '00'
def encrypt(key, plain_text):
    key_hex = ascii_string_to_hex_array(key)
    plain_hex = ascii_string_to_hex_array(plain_text)

    cypher_hex_str = ''
    for idx, ph in enumerate(plain_hex):
        # xor plain text and key
        cypher_hex_str += int_to_hex_str(int(ph, 16) ^ int(key_hex[idx % len(key_hex)], 16))

    return cypher_hex_str


def decrypt(cypher_text, key):
    plain_text = ''
    for idx, c in cypher_text:
        plain_text += int()


def get_streams_for_key_len(cypher_array, key_len):
    return dict(
        zip(
            [i for i in range(0, key_len)],
            [cypher_array[i::key_len] for i in range(0, key_len)]
        )
    )


# calculate average incidence of coincidence for streams
def get_average_stream_ic(streams):
    totals = defaultdict()
    for sIdx, stream in streams.items():
        totals[sIdx] = 0
        for c in (list(set(stream))):
            totals[sIdx] += (stream.count(c) / len(stream) - 1/255) ** 2

    return sum([val for v, val in totals.items()]) / len(totals)


def find_key_len():
    with open('cypher.txt', 'r') as f:
        cypher = f.read()
        # chunk cypher into array of 2 character strings
        # each element represents a single hex digit
        cypher_array = [cypher[i:i + 2] for i in range(0, len(cypher), 2)]
        # initialize storage
        candidates = defaultdict()
        totals = defaultdict()

        for key_len in range(2, 19):
            # get all streams for current key length
            candidates[key_len] = get_streams_for_key_len(cypher_array, key_len)
            # get ic for streams for current key length
            totals[key_len] = get_average_stream_ic(candidates[key_len])

            print('Key length: {}. Bytes: {}. IC: {}'.format(
                key_len,
                len(candidates[key_len].items()),
                totals[key_len]
            ))

    f.close()

    return max(totals.items())

probably_key_len = find_key_len()
print(f'It looks like the key length is {probably_key_len}, or {probably_key_len} is a multiple of the true key length')

# Assumptions:
# 1. cypher text is hex string as ascii bytes (2 cypher text characters == 1 hex cypher text nibble)
from collections import defaultdict


def ascii_string_to_hex_array(ascii_text):
    return [int_to_hex_str(ord(t)) for t in ascii_text]


# - convert int to a 2 byte hex string
# - strip 0x and pad with zeros to 2 characters
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


def find_key_len():
    with open('cypher.txt', 'r') as f:
        cypher = f.read()
        cypher_array = [cypher[i:i + 2] for i in range(0, len(cypher), 2)]
        candidates = defaultdict(dict)
        totals = defaultdict(dict)

        best = 0
        best_key_len = 0
        for key_len in range(2, 19):
            # get all streams for current key length
            candidates[key_len] = get_streams_for_key_len(cypher_array, key_len)

            for cIdx, streams in candidates.items():
                for sIdx, stream in streams.items():
                    totals[cIdx][sIdx] = 0
                    for c in (list(set(stream))):
                        totals[cIdx][sIdx] += (stream.count(c) / len(stream)) ** 2



            stream_average_ic = sum([val for v, val in totals[cIdx].items()]) / len(totals[cIdx])
            if stream_average_ic > best:
                best = stream_average_ic
                best_key_len = cIdx

            print('Key length: {}. Bytes: {}. IC: {}'.format(
                key_len,
                len(stream),
                stream_average_ic
            ))

    f.close()

    return best_key_len

key_len = find_key_len()
print(f'It looks like the key length is {key_len}, or {key_len} is a multiple of the true key length')

from vigenere_cracker import find_key_len, get_streams_for_key_len, get_cypher_array, get_stream_ic

with open('cypher.txt', 'r') as f:
    cypher = f.read().strip('\n')
    probable_key_len = find_key_len(cypher)
    print(f'It looks like the key length is {probable_key_len}, or {probable_key_len} is a multiple of the true key length')

    x = zip([i for i in range(32, 177)], [chr(i) for i in range(32, 177)])
    candidates = dict()

    streams = get_streams_for_key_len(get_cypher_array(cypher), 7)
    for stream in streams.values():
        for n in range(1, 255):
            distribution = [int(c, 16) ^ n for c in stream]

            if max(distribution) < 127 and min(distribution) > 32:
                # assign key value (n) array of alphabetic characters
                candidates[n] = [d for d in distribution if d in [*range(65, 90), *range(97, 122)]]



    f.close()

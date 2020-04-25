from vigenere_cracker import find_key_len

with open('cypher.txt', 'r') as f:
    cypher = f.read()
    probably_key_len = find_key_len(cypher)
    print(f'It looks like the key length is {probably_key_len}, or {probably_key_len} is a multiple of the true key length')

    f.close()

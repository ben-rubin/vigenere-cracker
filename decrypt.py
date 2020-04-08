# each byte in hex is represented as a 2 character string
chunkLen = 2

with open('cypher.txt', 'r') as f:
    for keyLen in range(1, 14):
        count = 1

        print('--------')
        print("keyLen: {}".format(keyLen))

        while True:
            # seek to last chunk of key
            f.seek(keyLen * chunkLen * count - chunkLen)
            # read last chunk of key
            chunk = f.read(chunkLen)

            # passed end of cypher text
            if not chunk:
                break

            # convert to integer as if it were hex
            num = int(chunk, 16)

            count += 1
            print(chunk)

f.close()

from collections import defaultdict
# each byte in hex is represented as a 2 character string
# key is measured in multiples of chunkLen
# i.e. key length of 1 means key is 1 chunkLen or 2 characters or 1 hex byte
chunkLen = 2
# assume text and key is in printable ascii character range
candidates = range(32, 127)
xored = defaultdict(dict)

with open('cypher.txt', 'r') as f:
    cypher = f.read()
    cypherArray = [cypher[i:i + chunkLen] for i in range(0, len(cypher), chunkLen)]
    p = defaultdict(dict)


    # assume key length is at least 2
    for keyLen in range(1, 14):
        count = 1

        selection = []
        totalTotal = 0
        while True and len(cypherArray) > keyLen * count - 1:
            # go to start of last chunk of key
            #f.seek(keyLen * chunkLen * count - chunkLen)
            #chunk = f.read(chunkLen)
            chunk = cypherArray[keyLen * count - 1]
            selection.append(chunk)
            # passed end of cypher text
            #if not chunk:
            #    break

            # convert to integer as if it were hex
            #num = int(chunk, 16)

            # try getting
            # calculate incidence of occurrence using sum of squares
            # iterate over every Nth character up to N == keyLen
            count += 1

        pL = defaultdict()
        pL['total'] = 0
        for s in list(set(selection)):
            #pL[s] = selection.count(s) / len(selection)
            pL['total'] += (selection.count(s) / len(selection) - 1/255) ** 2

        print(pL)

        #pL['total'] += ((1 / len(selection) - 1/256) ** 2)
        #totalTotal += pL['total']
        #print('key length: {} , frequency: {}'.format(keyLen, pL['total']))
        #For each keyLen:keyLen
        #    select every Nth character. For each character, calculate its frequency in the selection
        #    - repeat every Nth character selection until all charcters have been selected, and sum frequencies
        #    - sum using (frequency[i] - 1/256) ^ 2


            # we want to find the
            # for c in candidates:
            #   plainText = c ^ num
            #  if 31 < plainText < 48 < plainText < 58 < plainText < 127:
            #     xored[c][count] = plainText

            #count += 1
            #print(chunk)

f.close()

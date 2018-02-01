def counting(l):
    result = list()

    col = 0
    uni = len(set(l))

    for i in range(1, len(l)+1):
        for j in range(i, len(l)):
            if (l[i-1] != l[j]):
                col = col +1

    result.append(col)
    result.append(uni)
    return result

n = int(input())

while(n != 0):
    coll = 0
    uniques = 0

    hashingDict = {}

    for i in range(n):
        fileString = input()
        h = 0
        for letter in fileString:
            h ^= ord(letter)

        if h not in hashingDict:
            hashingDict[h] = []
        hashingDict[h].append(fileString)

    for j in hashingDict.keys():
        amounts = counting(hashingDict[j])
        a = amounts[0]
        b = amounts[1]
        uniques += b
        coll += a

    print(str(uniques) + " " + str(coll))

    n = int(input())

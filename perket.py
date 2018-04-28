def diff(bit, S, B):
    sour = 1
    bitter = 0

    i = 0
    while(bit):
        if(bit & 1):
            sour *= S[i]
            bitter += B[i]
        i += 1
        bit >>= 1

    if(sour - bitter > 0):
        return sour - bitter
    else: return bitter - sour


n = int(input())

sour = []
bitt = []

minD = 1000000000


for i in range(n):
    S, B = list(map(int, input().split()))
    sour.append(S)
    bitt.append(B)

for i in range(1, 1<<n):
    result = diff(i, sour, bitt)
    if(result < minD):
        minD = result
    if(minD == 0):
        print(0)
        exit()



print(minD)

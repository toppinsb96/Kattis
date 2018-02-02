def checkSq(M):
    if(int(M**(1/2))**2 == M):
        return int(M**(1/2))
    else:
        return int(M**(1/2)) + 1


number = int(input())

for msg in range(number):

    message = input()

    L = len(message)
    K = checkSq(L)
    M = K ** 2
    result = ""

    for i in range(M - L):
        message += "*"

    for i in range(K):
        loc = M
        for i in range(K):
            if(message[loc - K] != "*"):
                result += message[loc - K]
            loc -= K
        M += 1

    print(result)

def doCollatz(x):
    L = list()
    while(True):
        L.append(x)
        if(x == 1):
            break
        if(x%2 == 0):
            x = x/2
        else:
            x = x*3+1

    return L

def meet(L1, L2, a, b):

    i = 0
    for i in L1:
        if i in L2:
            indexA = L1.index(i)
            indexB = L2.index(i)
            break
    i = int(i)
    print(a + " needs " + str(indexA) + " steps, " + b + " needs " + str(indexB) + " steps, they meet at " + str(i))

while(True):
    numbers = input().split()

    if(int(numbers[0]) == 0 | int(numbers[1]) == 0):
        break

    L1 = doCollatz(int(numbers[0]))
    L2 = doCollatz(int(numbers[1]))
    meet(L1, L2, numbers[0], numbers[1])

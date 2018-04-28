T = int(input())

# Recursively descend backwards from N by the power of 2.
def hadamard(n, x, y):
    newN = n/2

    if(n == 1): return 1

    elif(x > (n/2) - 1 and y > (n/2) - 1):
        x -= n/2
        y -= n/2
        return -hadamard(newN, x, y)
    else:
        x %= n/2
        y %= n/2
        return  hadamard(newN, x, y)

def printMatrix(n, x, y, w, h):
    # Set up 2D image
    for j in range(h):
        for k in range(w):
            # offset the the j and k by the x and y values
            print(str(hadamard(n, x + k, y + j)) + " ", end='')
        print()
    if T > 0 : print()

for i in range(T):
    n, x, y, w, h = map(int, input().split())
    printMatrix(n, x, y, w, h)

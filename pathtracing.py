import sys

def down(a, xi, xy):
    return a + [["*"]]
def up(a, xi, xy):
    return [["*"]] + a
def left(a, xi, xy):
    l = ["*"]
def right(a, xi, xy):
    print("HOLDER")


Path2D = [["S"]]
x = 1
y = 1
for line in sys.stdin:
    for i in range(x):
        if(line == "down\n"):
            print("down")
        if(line == "up\n"):
            print("up")
            
        for j in range(y):
            if(line == "left\n"):
                print("left")
            if(line == "right\n"):
                print("right")




"""
for i in range(3):
    for j in range(3):
        print(Path2D[i][j], end = '')
    print()
"""

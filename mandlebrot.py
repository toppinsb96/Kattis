import sys
import math

cnt = 1
for line in sys.stdin.readlines():
    cases = line.split()
    num = cases[2]
    div = False

    x = 0
    y = 0

    for i in range(int(num)):
        t = x
        x = x**2 - y**2 + float(cases[0])
        y = 2*t*y + float(cases[1])

        if(abs(math.sqrt(x**2 + y**2)) > 2):
            div = True
            break
    if(div):
        print("Case " + str(cnt) + ": " + "OUT")
    else:
        print("Case " + str(cnt) + ": " + "IN")

    cnt += 1

import sys
import math

for line in sys.stdin:
    i = float(line)
    if(i > 1):
        print(math.floor(math.log(math.sqrt(i*2.0*math.pi),10) + i*math.log(i/math.e,10) + 1))
    else:
        print(1)

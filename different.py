import sys

for line in sys.stdin:
    result = line.split()
    print(abs(int(result[0])-int(result[1])))

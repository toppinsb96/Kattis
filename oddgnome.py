n = int(input())

for i in range(n):
    line = list(map(int, input().split()))
    m = line[0]
    curIt = line[1];
    for j in range(2, line[0]):
        if(curIt + 1 != line[j]):
            print(j)
            break;
        curIt += 1

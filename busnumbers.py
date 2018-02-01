def organize(l, num):
    l.append("TEMPORARY")
    result = []

    cnt = 1
    prevBus = l[0]
    for i in range(num + 1):
        currBus = l[i]
        if(currBus == prevBus + 1):
            cnt += 1
        else:
            if(cnt == 1):
                result.append(l[i-1])
            if(cnt == 2):
                result.append(l[i-2])
                result.append(l[i-1])
            if(cnt >= 3):
                result.append(str(l[i-cnt]) + "-" + str(l[i-1]))
            cnt = 1
        prevBus = currBus
    result.pop(0)
    return result

def prettyPrint(l):
    s = ""
    for i in range(len(l)):
        s += str(l[i]) + " "
    print(s.rstrip())


num = int(input())
busList = sorted(map(int, input().split()))
prettyPrint(organize(busList, num))

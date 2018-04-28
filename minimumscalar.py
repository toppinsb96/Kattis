import itertools

T = int(input())

c = 1;

for cases in range(T):
    coor = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    amt = 0
    v1.sort()
    v2.sort(reverse = True)
    for i in range(coor):
        amt += v1[i] * v2[i]

    print("Case #" + str(c) + ": " + str(amt))
    c+=1

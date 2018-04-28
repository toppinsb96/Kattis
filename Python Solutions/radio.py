N,P = list(map(int, input().split()))
V = list(map(int, input().split()))

result = 0;

for i in range(len(V)):
    profit = 0;
    for j in range(i,len(V)):
        profit += (V[j] - P)
        if(profit > result):
            result = profit


print(result)

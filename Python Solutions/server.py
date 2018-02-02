amount = list(map(int, input().strip().split()))
times = list(map(int, input().strip().split()))

n = amount[0]
T = amount[1]
testingAmt = 0
result = 0

for i in range(n):
    if(testingAmt + times[i] > T):
        break
    testingAmt += times[i]
    result += 1

print(result)

from collections import defaultdict
from heapq import *

N, T = list(map(int, input().split()))
customerQ = defaultdict(list)

for i in range(N):
    money, time = list(map(int, input().split()))
    customerQ[time].append(money)

amt = 0
pool = []



for t in range(T, -1, -1):
    m = 0
    for price in customerQ[t]:
        pool.append(price)

    pool.sort()

    if(pool):
        amt += pool.pop()

print(amt)

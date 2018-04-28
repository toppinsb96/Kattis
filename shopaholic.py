n = int(input())
items = sorted(list(map(int, input().split())), reverse=True)
# Reverse Sort for Greedy Approach
t = 0
i = 0

while(i < n - 2):
    t += items[i + 2]
    i += 3

print(t)

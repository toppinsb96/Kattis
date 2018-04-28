N = int(input())
fruit = list(map(int, input().split()))
sum = 0
# EdgeCase: For all items 4 or more, they're immediately added to the sum
# Calculation for amount of each fruit will be added max end sum
if(N > 3):
    for i in range(N):
        sum += int(2**N - 2**N/2 - (N-1) * (N-2) / 2 - (N-1) - 1)*fruit[i]

# Summing the threes since a basket can only ever have three items in it.
for i in range(N):
    if(fruit[i] >= 200): sum+=fruit[i]
    for j in range(i):
        if(fruit[i] + fruit[j] >= 200) : sum += fruit[i] + fruit[j]
        for k in range(j):
            if(fruit[i] + fruit[j] + fruit[k] >= 200) : sum += fruit[i] + fruit[j] + fruit[k]






print(sum)

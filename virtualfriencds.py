def union(a, b):
    a = find(a)
    b = find(b)

    if a == b: return amount[a]

    amount[a] = amount[a] + amount[b]
    amount[b] = amount[a]
    friend[a] = b

    return amount[a]

def find(a):
    if a not in friend:
        friend[a] = a
        amount[a] = 1
    if a == friend[a]:
        return a
    friend[a] = find(friend[a])
    return friend[a]





T = int(input())

for i in range(T):
    # running dictionary of friends and the amount of friends they have
    friend = {}
    amount = {}
    n = int(input())
    for i in range(n):
        a, b = list(map(str, input().split()))
        ans = union(a, b)
        print(ans)

component = {}
count = {}


def find(x):
    if x not in component:
        component[x] = x
        count[x] = 1

    if x == component[x]:
        return x
    else:
        component[x] = find(component[x])
        return component[x]


def union(x, y):
    xx = find(x)
    yy = find(y)

    if xx != yy:
        component[xx] = yy
        count[xx] = count[xx] + count[yy]
        count[yy] = count[xx]

    return count[xx]


T = int(input())
for t in range(T):
    F = int(input())
    component.clear()
    count.clear()

    for f in range(F):
        x, y = input().split()
        ans = union(x,y)
        print(ans)

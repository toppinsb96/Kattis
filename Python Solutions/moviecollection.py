n = int(input())

for i in range(n):
    mr = input().split()
    m = int(mr[0])
    r = int(mr[1])
    stack = [None] * m
    movies = input().split()

    for j in movies:
        if j not in stack:
            stack[int(j)-1] = j

    for k in movies:
        print(stack.index(k), end = " ")
        stack.remove(k)
        stack = [k] + stack

    print()

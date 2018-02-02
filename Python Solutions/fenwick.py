def sum(tree, i):
    res = 0

    while i > 0:
        res += tree[i]
        i -= i & (-i)

    return res

def update(tree , N , i, val):
    i += 1

    while i <= N:
        tree[i] += val
        i += i & (-i)


def main():
    N,Q = map(int, input().split())
    ftTree = [0] * (N + 1)

    for i in range(Q):
        command = input().split()
        if(command[0] == "+"):
            update(ftTree, N, int(command[1]), int(command[2]))
        if(command[0] == "?"):
            print(sum(ftTree, int(command[1])))

main()

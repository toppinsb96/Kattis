X,Y = list(map(int, input().split()))
N = int(input())

t = 0
for i in range(N):
    s = list(map(float, input().split()))
    t += (s[1] - s[0]) * s[2]
    Y -= (s[1] - s[0])

print(X/(t + Y))

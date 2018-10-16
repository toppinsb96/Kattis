N, T = list(map(int, input().split()))
A,B,C,t = list(map(int, input().split()))


amt = 0
pen = 0


times = []
times.append(t)
for i in range(1,N):
    times.append((((A * times[i-1]) + B) % C) + 1)

times.sort()
curr = T
for i in times:
    if(curr < i):
        break;

    amt += 1
    curr -= i

    pen += (T - curr)
    pen %= 1000000007

print(str(amt) + " " + str(pen))

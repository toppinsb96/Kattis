n = int(input()) + 1
cats = {0: 1}


for k in range(n):
    m = 4*k + 2
    c = cats[k]*m
    cats[k+1]= c // (k+2)


print(cats[n])

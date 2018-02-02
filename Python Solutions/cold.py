
num = int(input())
temp = input().split()
count = 0
for i in range(num):
    if(int(temp[i]) < 0):
        count += 1
print(count)

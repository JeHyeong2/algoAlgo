n = int(input())

now = 0
count = 0
for i in range(1,n+3):
    if now <= n:
        now += i
        count+=1
    else:
        print(count-1)
        break

K = int(input())

a1 = 1
n =1
count = 0
while n < K:
    n *= 2
    a1 *=2
while K >= 0:
    if K - n == 0:
        break
    if K - n//2 >0:
        K -= n//2
    n = n//2
    count+=1
print(a1,count)
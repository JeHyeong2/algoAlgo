N = int(input())

info = list(map(int,input().split()))


ans = [99] * N
num = 1

for i in range(N):
    count = 0
    for j in range(N):
        if count == info[i]:
            if ans[j] < num:
                continue
            ans[j] = num
            break
        if ans[j] > num:
            count +=1
    num +=1
print(*ans)
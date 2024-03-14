N , M = map(int,input().split())
nlist = list(map(int,input().split()))

ans = []
for i in nlist:
    if i < M:
        ans.append(i)

print(*ans)
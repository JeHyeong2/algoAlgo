import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = {}

for i in range(N):
    newone = input().rstrip()
    if len(newone) < M:
        continue
    else:
        if newone not in ans:
            ans[newone] = 1
        else:
            ans[newone] += 1

new_ans = sorted(ans,key= lambda x:(-ans[x],-len(x),x))

print(*new_ans)
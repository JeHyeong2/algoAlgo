N,M = map(int,input().split())

l = [i for i in range(1,N+1)]

for i in range(M):
    a, b = map(int,input().split())
    tmp1 = l[a-1]
    tmp2 = l[b-1]
    l[a-1] = tmp2
    l[b-1] = tmp1
print(*l)
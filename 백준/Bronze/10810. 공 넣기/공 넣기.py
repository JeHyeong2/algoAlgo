N, M = map(int,input().split())
basket = [0]*(N+1)

for i in range(M):
    a,b,c = map(int,input().split())
    for j in range(a,b+1):
        basket[j] = c
basket.pop(0)
print(*basket)
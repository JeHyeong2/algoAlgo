import sys
input = sys.stdin.readline
N,M = map(int,input().split())
buket = [i for i in range(1,N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    tmp1 = buket[a-1:b]
    tmp1.reverse()
    buket[a-1:b] = tmp1

print(*buket)
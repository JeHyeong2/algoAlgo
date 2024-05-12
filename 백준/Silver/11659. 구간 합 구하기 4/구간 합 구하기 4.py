import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nums = list(map(int,input().split()))

_sum = [0] * N

s = 0
for i in range(N):
    s += nums[i]
    _sum[i] = s

for i in range(M):
    a, b = map(int,input().split())
    if a > 1:
        print(_sum[b-1] - _sum[a-2])
    else:
        print(_sum[b-1])
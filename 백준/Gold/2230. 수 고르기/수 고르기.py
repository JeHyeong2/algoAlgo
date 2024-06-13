import sys
input =sys.stdin.readline
N, M = map(int,input().split())
nl = []
for _ in range(N):
    a = int(input())
    nl.append(a)

nl.sort()

_min = 2e9

left = 0
right = 0
while left <= N-1 and right <= N-1:
    if nl[right] - nl[left] == M:
        _min = M
        break
    if nl[right] - nl[left] < M:
        right += 1
    elif nl[right] - nl[left] > M:
        if _min > nl[right] - nl[left]:
            _min = nl[right] - nl[left]
        left +=1
print(_min)


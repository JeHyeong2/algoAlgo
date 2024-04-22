from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

numlist = list(map(int,input().split()))

sortedlist = sorted(numlist)
plist =[-1] *N
pdic = {}

blist = [-1] * N

for i in range(N):
    plist[i] = sortedlist[i]
    if numlist[i] not in pdic:
        pdic[numlist[i]] = deque()
        pdic[numlist[i]].append(i)
    else:
        pdic[numlist[i]].append(i)

for i in range(N):
    blist[pdic[plist[i]].popleft()] = i


print(*blist)
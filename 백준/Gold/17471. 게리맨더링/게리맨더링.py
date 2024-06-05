from copy import deepcopy
import sys
input =sys.stdin.readline
def garry(arr):
    global ans
    if arr.count(1) == N or arr.count(1) == 0:
        return
    c1 = []
    c2 = []
    area1 = 0
    area2 = 0
    checker = [0] * (N+1)

    for i in range(1,N+1):
        if arr[i]:
            c1.append(i)
        else:
            c2.append(i)
    q = [c1[0]]
    checker[c1[0]] = 9
    while q:
        s = q.pop()
        for i in info[s]:
            if i in c1 and not checker[i]:
                checker[i] = 9
                q.append(i)
    q = [c2[0]]
    checker[c2[0]] = 9
    while q:
        s = q.pop()
        for i in info[s]:
            if i in c2 and not checker[i]:
                checker[i] = 9
                q.append(i)

    if checker.count(9) == N:
        for i in range(1,N+1):
            if arr[i] == 1:
                area1 += population[i]
            else:
                area2 += population[i]
        if abs(area1 - area2) < ans:
            ans = abs(area1 - area2)
            return
    return



def find_c(visit,s):
    v = deepcopy(visit)
    garry(v)
    for i in range(s,N+1):
        if not v[i]:
            v[i] = 1
            find_c(v,i)
            v[i] = 0
    return

N = int(input())
population = [0] + list(map(int,input().split()))

info = {}
ans=1001
for i in range(1,N+1):
    a = list(map(int,input().split()))
    if i not in info:
        info[i] = []
    for j in range(1,a[0]+1):
        info[i].append(a[j])

visited = [0] * (N+1)

find_c(visited,1)
if ans != 1001:
    print(ans)
else:
    print(-1)
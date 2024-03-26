import heapq
import sys
input = sys.stdin.readline

N = int(input())
lastday = 0
paylist = {}
ans = 0
for _ in range(N):
    pay,day = map(int,input().split())
    if day not in paylist:
        paylist[day] = [pay]
    else:
        paylist[day].append(pay)
    if day > lastday:
        lastday = day

h = []
heapq.heapify(h)
for i in range(lastday,0,-1):
    if i in paylist:
        for j in paylist[i]:
            heapq.heappush(h,-j)
    if h:
        ans += -heapq.heappop(h)


print(ans)

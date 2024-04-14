from collections import deque
import heapq
import sys
input = sys.stdin.readline
N = int(input())

skyline = [map(int,input().split()) for _ in range(N)]
count = 0
q = []
heapq.heapify(q)
for i,j in skyline:
    if not q and j != 0:
        q.append(-j)
    else:
        if q:
            if q[0] < -j:
                while q and q[0] < -j:
                    count+=1
                    heapq.heappop(q)
                if q:
                    if q[0] > -j:
                        heapq.heappush(q, -j)
            elif q[0] > -j:
                heapq.heappush(q,-j)
            if not q and j!=0:
                heapq.heappush(q,-j)

else:
    while q:
        heapq.heappop(q)
        count+=1

print(count)

import heapq
import sys
input = sys.stdin.readline

def djikstar(start):
    visited = [0] * (N+1)
    weight = [0] * (N + 1)
    h = [(-inf,start)]
    heapq.heapify(h)
    weight[start] = -inf
    while h:
        last_cost, now = heapq.heappop(h)
        if last_cost < weight[now]:
            weight[now] = last_cost
        for n,c in info[now].items():
            next_node,next_cost = n,c
            if not visited[next_node]:
                if next_cost > last_cost:
                    heapq.heappush(h,(next_cost,next_node))
                else:
                    heapq.heappush(h,(last_cost,next_node))
        visited[now] = 1
    return -weight[destination[1]]

N,M = map(int,input().split())
info = {}

inf= 1000000001

for i in range(M):
    s,e,c, = map(int,input().split())
    if s not in info:
        info[s] = {e:-c}
    else:
        if e not in info[s]:
            info[s][e] = -c
        else:
            if info[s][e] > -c:
                info[s][e] = -c
    if e not in info:
        info[e] = {s:-c}
    else:
        if s not in info[e]:
            info[e][s] = -c
        else:
            if info[e][s] > -c:
                info[e][s] = -c

destination = list(map(int,input().split()))
print(djikstar(destination[0]))

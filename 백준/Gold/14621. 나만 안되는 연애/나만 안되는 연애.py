import heapq
import sys
input = sys.stdin.readline
# 5 7
# M W W W M
# 1 2 12
# 1 3 10
# 4 2 5
# 5 2 5
# 2 5 10
# 3 4 3
# 5 4 7
def prim():
    h = []
    heapq.heapify(h)
    visited = [INF] * N
    heapq.heappush(h,(0,0))

    while h:
        cost, now = heapq.heappop(h)
        if visited[now] != INF:
            continue
        visited[now] = cost
        for i in road_info[now]:
            if visited[i[0]] == INF:
                heapq.heappush(h,(i[1],i[0]))

    for i in range(1,N):
        if visited[i] == INF:
            print(-1)
            return
    print(sum(visited))


N, M = map(int,input().split())
uni = list(map(str,input().split()))
INF = 1e9
road_info = [[] for _ in range(N)]

for i in range(M):
    s,e,c = map(int,input().split())
    if uni[s-1] == uni[e-1]:
        continue
    road_info[s-1].append((e-1,c))
    road_info[e-1].append((s-1,c))

prim()
import sys
import heapq
input = sys.stdin.readline
def djikstra(start):

    way = [INF] *(N+1)
    h = []

    heapq.heappush(h,(0,start))
    way[start] = 0

    heapq.heapify(h)
    while h:
        value, now = heapq.heappop(h)

        if way[now] < value:
            continue

        for node,cost in graph[now]:
            if cost + way[now] < way[node]:
                heapq.heappush(h,(cost,node))
                way[node] = cost + way[now]
    return way


N, M, X = map(int,input().split())

INF = 1239129890
graph =[[] for _ in range(N+1)]

toX = [0] * (N+1)
for _ in range(M):
    s,e,v = map(int,input().split())
    graph[s].append((e,v))


a = djikstra(X)
ans = 0
for i in range(1,N+1):
    if i == X:
        continue
    else:
        b = djikstra(i)
        ans = max(ans, b[X] + a[i])

print(ans)
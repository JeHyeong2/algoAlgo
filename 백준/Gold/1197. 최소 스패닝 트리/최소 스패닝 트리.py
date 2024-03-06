import sys
import heapq
input = sys.stdin.readline

def prim():
    ans = []
    start = list(graph.keys())[0]
    h = []
    visited = [False] * (N+1)
    for i in graph[start]:
        h.append(i)
    heapq.heapify(h)
    visited[start] = True
    while h:
        cost, next_node = heapq.heappop(h)
        if visited[next_node]:
            continue
        visited[next_node] = True
        ans.append(cost)
        for wt, nn in graph[next_node]:
            if not visited[nn]:
                heapq.heappush(h,(wt,nn))
    print(sum(ans))

N, M = map(int,input().split())

INF = 2147483648
graph = {}

weight = [[INF] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((c,b))
    graph[b].append((c,a))

prim()
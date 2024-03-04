import heapq
import sys
input = sys.stdin.readline
def prim(node):
    route =[]
    visited = [False] * (N+1)
    startnode = list(nodeinfo.keys())[0]
    edges = [(cost,next_node) for cost,next_node in node[startnode]]
    heapq.heapify(edges)
    visited[startnode] = True

    while edges:
        cost, end_node = heapq.heappop(edges)
        if not visited[end_node]:
            visited[end_node] = True
            route.append(cost)

            for cost, next_node in node[end_node]:
                if not visited[next_node]:
                    heapq.heappush(edges,(cost,next_node))

    if sum(route) == 0:
        print(-1)
        return
    count = 0
    for i in visited:
        if i == True:
            count +=1
    if count == N:
        print(sum(route))
    else:
        print(-1)
    return

N, M = map(int,input().split())

uni = list(map(str,input().split()))
university = [0]
for i in uni:
    university.append(i)

nodeinfo = {}

for i in range(M):
    a,b,c = map(int,input().split())
    if a not in nodeinfo:
        nodeinfo[a] = []
    if b not in nodeinfo:
        nodeinfo[b] = []
    if university[a] != university[b]:
        nodeinfo[a].append((c,b))
        nodeinfo[b].append((c,a))

prim(nodeinfo)
import heapq
import sys
input = sys.stdin.readline

def djikstra(s):
    short_route[s] = 0
    h = []
    h.append((0,s))
    heapq.heapify(h)
    while h:
        cost, now_node = heapq.heappop(h)
        if short_route[now_node] < cost:
            continue
        for next_cost,next_node in node_info[now_node]:
            if short_route[now_node] + next_cost < short_route[next_node]:
                short_route[next_node] = short_route[now_node] + next_cost
                heapq.heappush(h,(short_route[next_node], next_node))

    return




V, E = map(int,input().split())
start = int(input())
INF = 1e9
node_info = [[] for _ in range(V+1)]
short_route = [INF] * (V+1)
for _ in range(E):
    a,b,c = map(int,input().split())
    node_info[a].append((c,b))

djikstra(start)

for i in range(1, V + 1):
    if INF == short_route[i]:
        print("INF")
    else:
        print(short_route[i])
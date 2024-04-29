import heapq
def djikstra(start):
    h = []
    weight = [INF] * (D+1)
    heapq.heapify(h)
    weight[start] = 0
    heapq.heappush(h,(0,start))

    while h:
        dist, now = heapq.heappop(h)
        if weight[now] < dist:
            continue
        for i in road_info[now]:
            cost = weight[now] + i[1]
            if cost < weight[i[0]]:
                weight[i[0]] = cost
                heapq.heappush(h,(cost,i[0]))
    print(weight[-1])

N, D = map(int,input().split())
INF = 10e9
road_info = [[] for i in range(D+1)]

for i in range(N):
    s,e,c = map(int,input().split())
    if e > D:
        continue
    road_info[s].append((e,c))

for i in range(D):
    road_info[i].append((i+1,1))

djikstra(0)

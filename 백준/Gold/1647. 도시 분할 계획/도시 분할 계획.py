import heapq
import sys
input = sys.stdin.readline

def prim(dic):
    primedlist = []
    visited = [False] * (N+1)
    start_node = list(dic.keys())[0]
    visited[start_node] = True
    quelist = [(cost ,end_node) for end_node, cost in dic[start_node]]
    heapq.heapify(quelist)

    while quelist:
        cost, end_node = heapq.heappop(quelist)
        if not visited[end_node]:
            visited[end_node] = True
            primedlist.append(cost)

            if end_node in dic:
                for next_end , next_cost in dic[end_node]:
                    if not visited[next_end]:
                        heapq.heappush(quelist,(next_cost,next_end))
    return primedlist


N, M = map(int,input().split())
dicvilla = {}
ans = []

for _ in range(M):
    a,b,c = map(int,input().split())
    if M == 1:
       break
    if a not in dicvilla:
        dicvilla[a] = []
    if b not in dicvilla:
        dicvilla[b] = []
    dicvilla[a].append((b,c))
    dicvilla[b].append((a,c))

answer = 0
if M != 1:
    a= prim(dicvilla)
    answer = sum(a) - max(a)


print(answer)



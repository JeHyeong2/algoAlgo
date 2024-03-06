import sys
import heapq
input = sys.stdin.readline
#
# def djik(start):
#     short_route[start] = 0
#     h = []
#     h.append((0,start))
#     heapq.heapify(h)
#
#     count = 0
#     while h:
#         cost, now = heapq.heappop(h)
#         if short_route[now] < cost:
#             continue
#         for nextcost, nextnode in node_info[now]:
#             if short_route[nextnode] > short_route[now] + nextcost:
#                 heapq.heappush(h,(nextcost,nextnode))
#                 short_route[nextnode] = short_route[now] + nextcost
#     return short_route
#
#


#
# a = djik(1)
# a= a[1:]
#
# for i in range(len(a)):
#     if a[i] != abs(a[i]):
#         print(-1)
#         break
# else:
#     for j in range(1,len(a)):
#         if a[j] == INF:
#             print(-1)
#         else:
#             print(a[j])
def bf(start):
    short_route[start] = 0

    for i in range(N):
        for j in range(M):
            now = node_info[j][0]
            next = node_info[j][1]
            cost = node_info[j][2]
            if short_route[now] != INF and short_route[next] > short_route[now] + cost:
                short_route[next] = short_route[now] + cost
                if i == N - 1:
                    return False
    return True



N, M = map(int,input().split())
INF = 9876987689769876
node_info = []

for _ in range(M):
    a,b,c = map(int,input().split())
    node_info.append((a,b,c))

short_route = [INF] * (N+1)

a = bf(1)
if a == False:
    print(-1)
else:
    for i in short_route[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)






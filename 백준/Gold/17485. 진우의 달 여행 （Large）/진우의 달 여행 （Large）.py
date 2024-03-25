import sys
input = sys.stdin.readline
# def bfs(start):
#     global _min
#     a1,a2 = start
#     q = [(a1,a2,-1,0)]
#     while q:
#         s1,s2,last_arrow,_sum = q.pop()
#         this_sum = _sum + space[s1][s2]
#
#         if this_sum > _min:
#             continue
#
#         if s1 == N-1:
#             if this_sum < _min:
#                 _min = this_sum
#
#         if s1 == 0:
#             for k in range(3):
#                 ni = s1 + dist[k][0]
#                 nj = s2 + dist[k][1]
#                 if 0 <= ni < N and 0 <= nj < M:
#                     q.append((ni,nj,k,this_sum))
#         else:
#             if sum_space[s1][s2][last_arrow] > this_sum:
#                 sum_space[s1][s2][last_arrow] = this_sum
#                 for k in range(3):
#                     ni = s1 + dist[k][0]
#                     nj = s2 + dist[k][1]
#                     if k != last_arrow and 0 <= ni < N and 0 <= nj < M:
#                         q.append((ni,nj,k,this_sum))
#             else:
#                 continue
#





N, M = map(int,input().split())

INF = 1e9
space = [list(map(int,input().split())) for _ in range(N)]
sum_space = [[[INF]*3 for _ in range(M)] for _ in range(N)]
_min = 120948120948192480
for i in range(M):
    if i - 1 >= 0:
        sum_space[1][i][0] = space[0][i-1] + space[1][i]
    if i + 1 < M:
        sum_space[1][i][2] = space[0][i+1] + space[1][i]
    sum_space[1][i][1] = space[0][i] + space[1][i]
ans = 89123801293801283

for i in range(2,N):
    for j in range(M):
        if j - 1 >= 0:
            sum_space[i][j][0] = min(sum_space[i-1][j-1][1],sum_space[i-1][j-1][2]) + space[i][j]
        if j + 1 < M:
            sum_space[i][j][2] = min(sum_space[i - 1][j + 1][1], sum_space[i - 1][j + 1][0]) + space[i][j]
        sum_space[i][j][1] = min(sum_space[i-1][j][0],sum_space[i-1][j][2]) + space[i][j]


for i in range(M):
    if min(sum_space[N-1][i]) < ans:
        ans = min(sum_space[N-1][i])
print(ans)

import sys
input = sys.stdin.readline

# def bfs(start):
#     global ans
#     visited = [[False]*(M+1) for _ in range(N+1)]
#     q = []
#     s1, s2 = start
#     q.append((s1,s2))
#     visited[s1][s2] = True
#     count = 1
#     while q:
#         x, y = q.pop()
#         for k in range(4):
#             ni = x + di[k]
#             nj = y + dj[k]
#             if 0 < ni <= N and 0 < nj <= M:
#                 if class_room[ni][nj] == 1 and not visited[ni][nj]:
#                     count += 1
#                     visited[ni][nj] = True
#                     q.append((ni,nj))
#     if count > ans:
#         ans = count


def bfs():
    global ans
    visited = [[0]*(M+1) for _ in range(N+1)]
    an = [0]*(K+1)
    q = []
    j = 1
    for i in food_map:
        a, b = i
        q.append((a,b,j))
        j += 1

    while q:
        x, y, idx = q.pop()
        if visited[x][y] != idx:
            an[idx] += 1
        visited[x][y] = idx
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 < ni <= N and 0 < nj <= M:
                if class_room[ni][nj] == 1 and visited[ni][nj] != idx:
                    q.append((ni,nj,idx))

    print(max(an))


N, M, K = map(int, input().split())

class_room = [[0]*(M+1) for _ in range(N+1)]

food_map = []
ans = 0
di = [-1,0,1,0]
dj = [0,1,0,-1]

for i in range(K):
    food_map.append(list(map(int,input().split())))

for i in food_map:
    a, b = i
    class_room[a][b] = 1

# for i in food_map:
#     bfs(i)
bfs()

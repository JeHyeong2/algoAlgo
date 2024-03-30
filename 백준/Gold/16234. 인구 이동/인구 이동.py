from collections import deque
import sys

input = sys.stdin.readline


# def move_country():
#     global end,count
#     stoped = True
#     visited = [[-1]*N for _ in range(N)]
#     weight = [[0]*2 for _ in range(N*N*4)]
#     q = deque()
#     q.append((0,0,0))
#     numcount = 0
#
#
#     while q:
#         s1,s2,country_num = q.popleft()
#
#         if visited[s1][s2] != -1:
#             continue
#         weight[country_num][0] += countries[s1][s2]
#         weight[country_num][1] +=1
#         visited[s1][s2] = country_num
#         for k in range(4):
#             ni = s1 + di[k]
#             nj = s2 + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 if L <= abs(countries[s1][s2] - countries[ni][nj]) <= R:
#                     q.appendleft((ni,nj,country_num))
#                 else:
#                     if visited[ni][nj] == -1:
#                         numcount += 1
#                         q.append((ni,nj,numcount))
#     for i in range(N):
#         for j in range(N):
#             if weight[visited[i][j]][1] > 1:
#                 countries[i][j] = weight[visited[i][j]][0] // weight[visited[i][j]][1]
#                 stoped = False
#     if stoped:
#         print(count)
#         end = False
#     else:
#         count +=1
#     return
def move_country():
    global end,count
    stoped = True
    visited = [[-1]*N for _ in range(N)]
    weight = {}
    q = deque()
    q.append((0,0,0))
    numcount = 0


    while q:
        s1,s2,country_num = q.popleft()

        if visited[s1][s2] != -1:
            continue
        if country_num not in weight:
            weight[country_num] = []
            weight[country_num].append(countries[s1][s2])
            weight[country_num].append(1)
        else:
            weight[country_num][0] += countries[s1][s2]
            weight[country_num][1] +=1
        visited[s1][s2] = country_num
        for k in range(4):
            ni = s1 + di[k]
            nj = s2 + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if L <= abs(countries[s1][s2] - countries[ni][nj]) <= R:
                    q.appendleft((ni,nj,country_num))
                else:
                    if visited[ni][nj] == -1:
                        numcount += 1
                        q.append((ni,nj,numcount))
    for i in range(N):
        for j in range(N):
            if weight[visited[i][j]][1] > 1:
                countries[i][j] = weight[visited[i][j]][0] // weight[visited[i][j]][1]
                stoped = False
    if stoped:
        print(count)
        end = False
    else:
        count +=1
    return







N,L,R = map(int,input().split())

di=[-1,0,1,0]
dj=[0,1,0,-1]
end= True
count = 0
countries = [list(map(int,input().split())) for _ in range(N)]
while end:
    move_country()
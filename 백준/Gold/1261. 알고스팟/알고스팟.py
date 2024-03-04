from collections import deque
import sys
input = sys.stdin.readline

def breakroom(room):
    Q = deque()
    visited[0][0] = 0
    Q.append((0, 0))
    while Q:
        s1,s2= Q.popleft()
        for k in range(4):
            ni = s1 + di[k]
            nj = s2 + dj[k]
            if 0 <= ni < M and 0 <= nj < N:
                if visited[ni][nj] == -1:
                    if room[ni][nj] == 0:
                        visited[ni][nj] = visited[s1][s2]
                        Q.appendleft((ni,nj))
                    else:
                        visited[ni][nj] = visited[s1][s2] +1
                        Q.append((ni,nj))




N, M = map(int,input().split())

room = []

for i in range(M):
    a = list(map(int,input().strip()))
    room.append(a)

visited = [[-1] * N for _ in range(M)]
di = [-1,0,1,0]
dj = [0,1,0,-1]

breakroom(room)
print(visited[M-1][N-1])
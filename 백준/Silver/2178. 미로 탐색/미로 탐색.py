import sys
input = sys.stdin.readline

def bfs():
    q = [(0,0)]
    visited[0][0] = 1
    while q:
        s1,s2 = q.pop()
        for k in range(4):
            ni = s1 + di[k]
            nj = s2 + dj[k]
            if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == 1 and visited[ni][nj] > visited[s1][s2]+1:
                visited[ni][nj] = visited[s1][s2] + 1
                q.append((ni,nj))





n,m = map(int,input().strip().split())

field = [list(map(int,(input().strip()))) for _ in range(n)]

visited =[[10001]*m for _ in range(n)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

bfs()
print(visited[n-1][m-1])
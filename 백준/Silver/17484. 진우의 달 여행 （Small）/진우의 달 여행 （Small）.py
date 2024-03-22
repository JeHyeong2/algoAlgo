def bfs(start,sum,direction):
    global _max
    a, b = start
    s = sum
    s += space[a][b]
    if s > _max:
        return
    if a == N-1:
        if s < _max:
            _max = s
    for i in range(1,4):
        if i != direction:
            ni = a + dist[i][0]
            nj = b + dist[i][1]
            if 0<= ni < N and 0 <= nj <M:
                bfs((ni,nj),s,i)

N, M = map(int,input().split())

space = [list(map(int,input().split())) for _ in range(N)]
_max = 120948120948192480


dist = [0,(1,-1),(1,0),(1,1)]
for i in range(M):
    bfs((0,i),0,0)

print(_max)
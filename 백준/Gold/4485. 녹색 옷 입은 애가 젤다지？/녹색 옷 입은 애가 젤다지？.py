import sys
import heapq
input = sys.stdin.readline
def djikstra():
    weight = [[INF]*N for _ in range(N)]
    start = (0,0)
    end = (N-1,N-1)
    h = []
    weight[0][0] = room[0][0]
    h.append((weight[0][0],start))
    heapq.heapify(h)
    while h:
        cost,(now_nodex,now_nodey) = heapq.heappop(h)
        if weight[now_nodex][now_nodey] < cost:
            continue
        for k in range(4):
            ni = now_nodex + di[k]
            nj = now_nodey + dj[k]
            if 0<= ni < N and 0 <= nj <N:
                nextcost = cost + room[ni][nj]
                if weight[ni][nj] > nextcost:
                    weight[ni][nj] = nextcost
                    heapq.heappush(h,(nextcost,(ni,nj)))
    print(f'Problem {tc}: {weight[N-1][N-1]}')



tc = 0
while True:
    tc +=1
    INF = 1e9
    N = int(input())
    if N == 0:
        break
    di = [-1,0,1,0]
    dj = [0,1,0,-1]
    room = []
    for i in range(N):
        a = list(map(int,input().split()))
        room.append(a)
    djikstra()


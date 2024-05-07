from collections import deque
import sys
input = sys.stdin.readline


def dfs(x, y):

    # 도착지점에 도달하면 1을 반환
    if x == N - 1 and y == M - 1:
        return 1

    # 이전에 도착했던 곳이라면 dp[x][y] 값 반환
    if maps[x][y] != -1:
        return maps[x][y]

    # 처음 온 곳이라면 0으로 초기화
    maps[x][y] = 0

    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < M and mountain[ni][nj] < mountain[x][y]:
            maps[x][y] += dfs(ni, nj)

    return maps[x][y]






N , M = map(int,input().split())
mountain = [list(map(int,input().split())) for _ in range(N)]
ans = 0
di = [0,-1,0,1]
dj = [-1,0,1,0]
maps = [[-1]*M for _ in range(N)]

print(dfs(0, 0))
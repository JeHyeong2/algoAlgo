from collections import deque
import sys
input = sys.stdin.readline
 
K = int(input())
W, H = map(int, input().split()) # 열, 행
board = [list(map(int, input().split())) for _ in range(H)]
 
# 말처럼 이동하는 경우
dx_knight = [-2, -1, 1, 2, 2, 1, -1, -2]
dy_knight = [1, 2, 2, 1, -1, -2, -2, -1]
 
# 원숭이 처럼 상하좌우로 이동하는 경우
dx_monkey = [0, 0, -1, 1]
dy_monkey = [1, -1, 0, 0]
 
def bfs():
    visited = [[[False] * (K+1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = True
    queue = deque([(0, 0, K, 0)])
 
    while queue:
        x, y, k, move = queue.popleft()
 
        # 목표 지점 도달
        if x == H-1 and y == W-1:
            return move
 
        # 말처럼 이동하는 경우 - k(남은 움직일 수 있는 이동 횟수)가 1 이상인지 확인
        if k:
            for i in range(8):
                nx = x + dx_knight[i]
                ny = y + dy_knight[i]
 
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k-1] and board[nx][ny] != 1:
                    visited[nx][ny][k-1] = True
                    queue.append((nx, ny, k-1, move+1)) # 말처럼 움직인 횟수 1 차감, 이동 횟수 1 증감
 
        # 원숭이 처럼 상하좌우로 이동하는 경우
        for i in range(4):
            nx = x + dx_monkey[i]
            ny = y + dy_monkey[i]
 
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k] and board[nx][ny] != 1:
                visited[nx][ny][k] = True
                queue.append((nx, ny, k, move+1))
    return -1
 
print(bfs())
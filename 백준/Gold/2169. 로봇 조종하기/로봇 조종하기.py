from collections import deque
import sys

input = sys.stdin.readline

def dp():
    global ans
    table = [[0] * M]
    right = [[0] * M]
    left = [[0] * M]
    tmp = 0
    for i in range(M):
        tmp += space[0][i]
        table[0][i] = tmp
    if N == 1:
        ans= table[0][-1]
        return
    if M == 1:
        tmp = 0
        for i in range(N):
            tmp += space[i][0]
        ans = tmp
        return

    for i in range(1,N):
        right[0][0] = table[0][0] + space[i][0]
        left[0][-1] = table[0][-1] + space[i][-1]
        rtmp = right[0][0]
        ltmp = left[0][-1]
        for j in range(1,M):
            rtmp = max((table[0][j]+space[i][j]),rtmp + space[i][j])
            right[0][j] = rtmp
            ltmp = max((table[0][-1-j] + space[i][-1-j]), ltmp + space[i][-1-j])
            left[0][-1-j] = ltmp
        for k in range(M):
            table[0][k] = max(left[0][k],right[0][k])
    ans = table[0][M-1]
    return

ans =-10000000
N, M = map(int,input().split())
INF = -10000000
space = [list(map(int,input().split())) for _ in range(N)]


dp()
print(ans)


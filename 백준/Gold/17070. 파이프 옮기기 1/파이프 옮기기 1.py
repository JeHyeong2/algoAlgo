from collections import deque
import sys
input = sys.stdin.readline

def move_pipe():
    global count
    Q = deque()
    Q.append((0,1,0))
    if pipeline[N-1][N-1] == 1:
        return
    while Q:
        d1,d2,dr = Q.pop()
        if (d1,d2) == (N-1,N-1):
            count += 1
        if dr == 0:
            #가로
            di,dj = direction[0]
            ni = d1 + di
            nj = d2 + dj
            if ni < N and nj < N:
                if pipeline[ni][nj] == 0:
                    Q.append((ni,nj,0))
            for i in range(3):
                di,dj = direction[i]
                ni = d1 + di
                nj = d2 + dj
                if ni < N and nj < N:
                    if pipeline[ni][nj] == 0:
                        continue
                    else:
                        break
                else:
                    break
            else:
                Q.append((d1+1,d2+1,1))
        if dr == 1:
            di,dj = direction[2]
            ni = d1 +di
            nj = d2 +dj
            if ni < N and nj < N:
                if pipeline[ni][nj] == 0:
                    Q.append((d1+1,d2,2))
            di, dj = direction[0]
            ni = d1 + di
            nj = d2 + dj
            if ni < N and nj < N:
                if pipeline[ni][nj] == 0:
                    Q.append((d1,d2+1,0))
            for i in range(3):
                di, dj = direction[i]
                ni = d1 + di
                nj = d2 + dj
                if ni < N and nj < N:
                    if pipeline[ni][nj] == 0:
                        continue
                    else:
                        break
                else:
                    break
            else:
                Q.append((d1 + 1, d2 + 1, 1))

        if dr == 2:
            di, dj = direction[2]
            ni = d1 + di
            nj = d2 + dj
            if ni < N and nj < N:
                if pipeline[ni][nj] == 0:
                    Q.append((d1+1,d2,2))
            for i in range(3):
                di, dj = direction[i]
                ni = d1 + di
                nj = d2 + dj
                if ni < N and nj < N:
                    if pipeline[ni][nj] == 0:
                        continue
                    else:
                        break
                else:
                    break
            else:
                Q.append((d1 + 1, d2 + 1, 1))
    return
        #0 가로 ,1 대각 , 2세로

N = int(input())
direction = [(0,1),(1,1),(1,0)]

pipeline = [list(map(int,input().split())) for _ in range(N)]

count = 0
move_pipe()

print(count)
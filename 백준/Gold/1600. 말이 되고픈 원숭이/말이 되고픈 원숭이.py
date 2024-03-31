from collections import deque
import sys

input = sys.stdin.readline

def move():
    global _min
    weight_field = [[[0]*(K+1) for _ in range(N)] for _ in range(M)]
    q = deque()
    q.append((0,0,0))
    weight_field[0][0][0]=1

    while q:
        s1,s2,horse_count = q.popleft()

        if (s1,s2) == (M-1,N-1):
            return weight_field[s1][s2][horse_count] -1 

        if horse_count < K:
            for w in range(8):
                hi = s1 + horse_x[w]
                hj = s2 + horse_y[w]
                if 0 <= hi < M and 0 <= hj < N and field[hi][hj] != 1:
                    if weight_field[hi][hj][horse_count+1] == 0:
                        weight_field[hi][hj][horse_count+1] = weight_field[s1][s2][horse_count]+1
                        q.append((hi, hj, horse_count+1))

        for k in range(4):
            ni = s1 + di[k]
            nj = s2 + dj[k]
            if 0 <= ni < M and 0 <= nj < N and field[ni][nj] != 1:
                if weight_field[ni][nj][horse_count] == 0:
                    weight_field[ni][nj][horse_count] = weight_field[s1][s2][horse_count]+1
                    q.append((ni,nj,horse_count))

    return -1






K = int(input())
N,M = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(M)]


horse_x = [-1,-2,-1,-2,1,2,1,2]
horse_y = [-2,-1,2,1,-2,-1,2,1]

di = [-1,0,1,0]
dj = [0,1,0,-1]


print(move())

import sys
input = sys.stdin.readline

def virus(map):
    global max_safety, ans
    new_lab = [[0] * M for _ in range(N)]
    virus_list = []
    count = 0
    for i in range(N):
        for j in range(M):
            new_lab[i][j] = map[i][j]
            if map[i][j] == 2:
                count +=1
                virus_list.append((i,j))
    while virus_list:
        if count > max_safety:
            return
        d1,d2 = virus_list.pop()
        for i in range(4):
            ni = d1 + di[i]
            nj = d2 + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if new_lab[ni][nj] == 0:
                    new_lab[ni][nj] = 2
                    count += 1
                    virus_list.append((ni,nj))
    ans_ = 0
    if count < max_safety:
        max_safety = count
        for i in range(N):
            for j in range(M):
                if new_lab[i][j] == 0:
                    ans_ +=1
        else:
            if ans_ > ans:
                ans = ans_
    return

def bulid(c,nm):
    if c == 3:
        virus(nm)
        return
    for i in range(N):
        for j in range(M):
            if nm[i][j] == 0:
                nm[i][j] = 1
                bulid(c+1,nm)
                nm[i][j] = 0

N, M = map(int,input().split())
safety = 0
ans = 0
vi = 0
di = [-1,0,1,0]
dj = [0,1,0,-1]
laboratory = [list(map(int,input().split())) for _ in range(N)]
max_safety = 1094872390659826

bulid(0,laboratory)

print(ans)



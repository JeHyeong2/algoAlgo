from copy import deepcopy

def nocc(cc):
    global ans
    new_space = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_space[i][j] = room[i][j]
    answer = 0
    for i in cc:
        a,b,c,d = i
        x0 = di[(0 + d) % 4]
        y0 = dj[(0 + d) % 4]
        x1 = di[(1 + d) % 4]
        y1 = dj[(1 + d) % 4]
        x2 = di[(2 + d) % 4]
        y2 = dj[(2 + d) % 4]
        x3 = di[(3 + d) % 4]
        y3 = dj[(3 + d) % 4]
        if c == 1:
            d1 = 1
            while True:
                ni = a + x1 * d1
                nj = b + y1 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 +=1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
        if c == 2:
            d1 = 1
            while True:
                ni = a + x1 * d1
                nj = b + y1 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
            while True:
                ni = a + x3 * d1
                nj = b + y3 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
        if c == 3:
            d1 = 1
            while True:
                ni = a + x0 * d1
                nj = b + y0 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
            while True:
                ni = a + x1 * d1
                nj = b + y1 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 +=1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
        if c == 4:
            d1 = 1
            while True:
                ni = a + x0 * d1
                nj = b + y0 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
            while True:
                ni = a + x1 * d1
                nj = b + y1 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
            while True:
                ni = a + x3 * d1
                nj = b + y3 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
        if c == 5:
            d1 = 1
            while True:
                ni = a + x0 * d1
                nj = b + y0 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
            while True:
                ni = a + x1 * d1
                nj = b + y1 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
            while True:
                ni = a + x2 * d1
                nj = b + y2 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
            while True:
                ni = a + x3 * d1
                nj = b + y3 * d1
                if 0 <= ni < N and 0 <= nj < M:
                    if new_space[ni][nj] != 6:
                        new_space[ni][nj] = "#"
                        d1 += 1
                    else:
                        d1 = 1
                        break
                else:
                    d1 = 1
                    break
    for i in range(N):
        for j in range(M):
            if new_space[i][j] == 0:
                answer += 1
    if answer < ans:
        ans = answer


def find_cc(ccinfo,visit):
    ncinfo = deepcopy(ccinfo)
    vt = deepcopy(visit)
    for i in range(len(ccinfo)):
        if not vt[i]:
            vt[i] = True
            for j in range(4):
                a,b,c,d = ncinfo[i]
                ncinfo[i] = a,b,c,j
                nocc(ncinfo)
                find_cc(ncinfo,vt)












N, M = map(int,input().split())

di = [-1,0,1,0]
dj = [0,1,0,-1]
room = []

cc = []
for i in range(N):
    info = list(map(int,input().split()))
    room.append(info)

for i in range(N):
    for j in range(M):
        if room[i][j] != 6 and room[i][j] != 0:
            cc.append((i,j,room[i][j],0))

ans = 223748573485783
vistied = [False] *len(cc)
find_cc(cc,vistied)
cnt = 0
if ans == 223748573485783:
    for i in range(N):
        for j in range(M):
            if room[i][j] == 0:
                cnt +=1
    print(cnt)
else:
    print(ans)
from collections import deque

def moving(m,a):
    global ans
    shootcount = 0
    newmap = deque([[0] * M for _ in range(N)])
    for i in range(N):
        for j in range(M):
            newmap[i][j] = m[i][j]
    for i in range(N):
        shootlist = shooting(newmap,a)
        for j in shootlist:
            if j:
                a1,a2 = j
                if newmap[a1][a2] != 0:
                    newmap[a1][a2] = 0
                    shootcount += 1
        for k in range(M):
            newmap[N-1][k] = 0
        tmp = newmap.pop()
        newmap.appendleft(tmp)
    if shootcount > ans:
        ans = shootcount




def shooting(map,archer):
    deathnote = []
    for k in range(3):
        death = 12480912489048
        dest = ()
        left = 12098
        for i in range(N):
            for j in range(M-1,-1,-1):
                if map[i][j] == 1:
                    tmp = abs(N-i) + abs(archer[k]-j)
                    if tmp <= D:
                        if tmp < death:
                            left = j
                            death = tmp
                            dest = (i,j)
                        elif tmp == death:
                            if j < left:
                                left = j
                                death = tmp
                                dest = (i, j)
        deathnote.append(dest)
    return deathnote


def Location(n,v,c):
    global archer
    visit = []
    for i in v:
        visit.append(i)
    if c == 3:
        loca = []
        for i in range(M):
            if visit[i]:
                loca.append(i)
        archer.append(loca)
        return
    for i in range(n,M):
        if v[i] == False:
            visit[i] = True
            Location(i,visit,c+1)
            visit[i] = False



N, M, D = map(int,input().split())

board = []
for i in range(N):
    line = list(map(int,input().split()))
    board.append(line)


visited = [False] * M
ans = 0
archer =[]
Location(0,visited,0)
for i in archer:
    moving(board,i)
print(ans)


# 5 C 3  해야함





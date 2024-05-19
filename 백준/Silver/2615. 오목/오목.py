import sys

input = sys.stdin.readline
def sero(start):
    global win,where
    #맨앞꺼 출력
    s1,s2 = start
    me = Omok[s1][s2]
    count = 1
    visited[s1][s2][0] = 1
    while True:
        ni, nj = s1+(1*count),s2
        if 0 <= ni < 19 and 0 <= nj < 19:
            if Omok[ni][nj] == me:
                visited[ni][nj][0] = 1
                count += 1
                continue
            else:
                break
        else:
            break
    if count == 5:
        win = me
        where = (s1+1,s2+1)
    return


def garo(start):
    #맨처음꺼 출력
    global win, where
    s1, s2 = start
    me = Omok[s1][s2]
    count = 1
    visited[s1][s2][1] = 1
    while True:
        ni, nj = s1 , s2+ (1 * count)
        if 0 <= ni < 19 and 0 <= nj < 19:
            if Omok[ni][nj] == me:
                visited[ni][nj][1] = 1
                count += 1
                continue
            else:
                break
        else:
            break
    if count == 5:
        win = me
        where = (s1+1, s2+1)
    return


def Rdegak(start):
    global win, where
    s1, s2 = start
    me = Omok[s1][s2]
    count = 1
    visited[s1][s2][2] = 1
    while True:
        ni, nj = s1 + (1 * count), s2 + (1 * count)
        if 0 <= ni < 19 and 0 <= nj < 19:
            if Omok[ni][nj] == me:
                visited[ni][nj][2] = 1
                count += 1
                continue
            else:
                break
        else:
            break
    if count == 5:
        win = me
        where = (s1+1, s2+1)
    return


def Ldegak(start):
    global win, where
    s1, s2 = start
    me = Omok[s1][s2]
    count = 1
    visited[s1][s2][3] = 1
    while True:
        ni, nj = s1 + (1 * count), s2 + (-1 * count)
        if 0 <= ni < 19 and 0 <= nj < 19:
            if Omok[ni][nj] == me:
                visited[ni][nj][3] = 1
                count += 1
                continue
            else:
                break
        else:
            break
    if count == 5:
        win = me
        where = (s1+5, s2-3)
    return

#세로 0 가로 1 오른대각 2 왼대각 3
Omok = [list(map(int,input().split())) for _ in range(19)]
win = 0
where = ()


visited = [[[0]*4 for _ in range(19)]  for _ in range(19)]


for i in range(19):
    for j in range(19):
        if Omok[i][j]:
            if not visited[i][j][0]:
                sero((i,j))
            if not visited[i][j][1]:
                garo((i,j))
            if not visited[i][j][2]:
                Rdegak((i,j))
            if not visited[i][j][3]:
                Ldegak((i,j))

if win != 0:
    print(win)
    print(*where)
else:
    print(0)
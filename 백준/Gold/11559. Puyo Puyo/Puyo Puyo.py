import sys
input = sys.stdin.readline
def buyo_check():
    global buyo_buyo,ans
    buyo = False
    visited =[[0]*N for _ in range(M)]
    boom = [0] * ((N*M)+1)
    num = 1
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and game[i][j] != ".":
                count = 1
                q = [(i,j)]
                visited[i][j] = num
                while q:
                    s1,s2 = q.pop()
                    for k in range(4):
                        ni = s1 + di[k]
                        nj = s2 + dj[k]
                        if 0 <= ni < M and 0 <= nj < N and game[ni][nj] == game[s1][s2] and not visited[ni][nj]:
                            count += 1
                            visited[ni][nj] = num
                            q.append((ni,nj))
                if count >= 4:
                    boom[num] = 1
                    buyo = True
                num += 1
    for i in range(M):
        for j in range(N-1,-1,-1):
            if boom[visited[i][j]]:
                game[i].pop(j)
                game[i].append(".")
    if buyo:
        ans +=1
    else:
        buyo_buyo = False

N = 12
M = 6

filed = [list(input()) for _ in range(N)]
ans = 0
game = [[] for _ in range(M)]
di = [-1,0,1,0]
dj = [0,1,0,-1]
buyo_buyo = True

for i in range(M):
    for j in range(N-1,-1,-1):
        game[i].append(filed[j][i])

while buyo_buyo:
    buyo_check()
print(ans)
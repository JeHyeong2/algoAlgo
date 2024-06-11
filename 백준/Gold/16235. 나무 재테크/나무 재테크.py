import sys
input = sys.stdin.readline

def spring():
    for i in range(N):
        for j in range(N):
            tree[i][j].sort()
            for k in range(len(tree[i][j])):
                if yang_boon[i][j] >= tree[i][j][k]:
                    yang_boon[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    for q in range(len(tree[i][j]) - k):
                        dead_tree[i][j].append(tree[i][j].pop())
                    break
    return

def summer():
    for i in range(N):
        for j in range(N):
            while dead_tree[i][j]:
                energy = dead_tree[i][j].pop()
                if energy // 2 > 0:
                    yang_boon[i][j] += energy // 2

    return

def fall():
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for q in range(8):
                        ni = i + di[q]
                        nj = j + dj[q]
                        if 0 <= ni < N and 0 <= nj < N:
                            tree[ni][nj].append(1)
    return

def winter():
    for i in range(N):
        for j in range(N):
            yang_boon[i][j] += add_yang_boon[i][j]
    return


N, M, K = map(int,input().split())

yang_boon = [[5]*N for _ in range(N)]
add_yang_boon = [list(map(int,input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
dead_tree = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a,b,c = map(int,input().split())
    tree[a-1][b-1].append(c)

di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]
ans = 0


for _ in range(K):
    spring()
    summer()
    fall()
    winter()


for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])

print(ans)
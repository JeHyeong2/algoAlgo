import sys
input = sys.stdin.readline

def find_chicken(visit,c,k):
    v = [0] * len(chicken)
    if c == M:
        send = []
        for i in range(len(chicken)):
            if visit[i] == 1:
                send.append(i)
        out_count.append(send)
        return

    for i in range(len(chicken)):
        v[i] = visit[i]

    for i in range(k,len(chicken)):
        if not v[i]:
            v[i] = 1
            find_chicken(v,c+1,i+1)
            v[i] = 0



N, M = map(int,input().split())
kfc = [list(map(int,input().split())) for _ in range(N)]


house = []
chicken = []
kfc_count = 0


for i in range(N):
    for j in range(N):
        if kfc[i][j] == 2:
            chicken.append((i,j))
            kfc_count += 1
        if kfc[i][j] == 1:
            house.append((i,j))

out_count = []

visited = [0] * len(chicken)

ans = 1273684617

if len(chicken) - M > 0:
    find_chicken(visited,0,0)
    for q in range(len(out_count)):
        tmpans = 0
        for i in range(len(house)):
            tmp = 1871928471
            for j in range(len(chicken)):
                if j not in out_count[q]:
                    continue
                if abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1]) < tmp:
                    tmp = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
            tmpans += tmp
        if tmpans < ans:
            ans = tmpans
else:
    ans = 0
    for i in range(len(house)):
        tmp = 187236482364
        for j in range(len(chicken)):
            if abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1]) < tmp:
                tmp = abs(house[i][0] - chicken[j][0]) + abs(house[i][1] - chicken[j][1])
        ans += tmp

print(ans)
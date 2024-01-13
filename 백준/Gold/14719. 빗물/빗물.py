H,W = map(int,input().split())
rain_map = [[0]*W for _ in range(H)]
map_des = list(map(int,input().split()))
for n,i in enumerate(map_des):
    for j in range(i-1,-1,-1):
        rain_map[j][n] = 1

ans = 0
for i in range(H):
    count = 0
    start_ = False
    end = False
    for j in range(W):
        if rain_map[i][j] == 1:
            start_ = True
        if start_ == True and rain_map[i][j] == 0:
            count += 1
        if start_ == True and rain_map[i][j] == 1:
            ans += count
            count =0


print(ans)









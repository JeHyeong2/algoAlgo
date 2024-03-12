import sys
input = sys.stdin.readline

N,M = map(int,input().split())

# M 은 정원
# N 은 플레이어 수 로 웨이팅 스타트

que = []

for i in range(N):
    a, b = map(str,input().split())
    a = int(a)
    if que:
        for j in range(len(que)):
            if (a-10) <= que[j][0][0] <= (a+10):
                if len(que[j]) < M:
                    que[j].append((a,b))
                    break
        else:
            que.append([(a,b)])
    else:
        que.append([(a,b)])

for i in que:
    b = sorted(i,key= lambda x:x[1])
    if len(b) == M:
        print("Started!")
        for a,b in b:
            print(a,b)
    else:
        print("Waiting!")
        for a,b in b:
            print(a,b)




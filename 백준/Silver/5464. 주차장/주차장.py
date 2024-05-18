from collections import deque
import sys
input = sys.stdin.readline

def park(car):
    global ans,full
    for i in range(1,len(parking)):
        if not parking[i]:
            parking[i] = car
            ans += fee[i] * cars[car]
            return
    else:
        full = True
        waiting.append(car)
        return

def depark(car):
    global ans
    for i in range(1,len(parking)):
        if abs(car) == parking[i]:
            parking[i] = 0
            if waiting:
                parking[i] = waiting.popleft()
                ans += cars[parking[i]] * fee[i]
            return


N, M = map(int,input().split())
ans = 0
fee = [0]
for i in range(N):
    fee.append(int(input()))

parking = [0] * (N+1)
cars =[0]
full = False

for i in range(M):
    cars.append(int(input()))

counting = [int(input()) for _ in range(M*2)]

waiting = deque()
for i in range(M*2):
    if full:
        if abs(counting[i]) != counting[i]:
            depark(counting[i])
        else:
            park(counting[i])
    else:
        if abs(counting[i]) != counting[i]:
            depark(counting[i])
        else:
            park(counting[i])


print(ans)


#공간 없으면 대기
# 공간 하나 or 없다가 나가면 그자리
# 아니면 번호가 작은순서
#도착 순서대로 대기
# 무게에 비례

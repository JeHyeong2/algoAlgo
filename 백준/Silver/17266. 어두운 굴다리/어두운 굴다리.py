import math
#설치할 가로등 갯수 M
# 가로등 위치 x
# 높이만큼 주위를 비출 수 있음
# 최소한의 높히로 모든길을 밝히자.
# 모든 가로등 높이가 같아야한다.
# 내가 있는곳 . 다음가로등 있는곳 의 중간이 최댓값이 되는것.
# 처음과 끝만 예외처리
N = int(input())
M = int(input())
location = list(map(int,input().split()))
location.sort()

biggest = 0

now_ = 0
start = location[0]
end = N - location[-1]

if start > end:
    biggest = start
else:
    biggest = end

for i in range(M):
    if i+1 < M:
        now = math.ceil((location[i+1] - location[i]) / 2)
        if now > biggest:
            biggest = now

print(biggest)
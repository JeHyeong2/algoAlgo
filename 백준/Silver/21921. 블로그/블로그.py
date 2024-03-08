import sys
input = sys.stdin.readline
N, X = map(int,input().split())

data = list(map(int,input().split()))
stacked_sum = [0] *N
stacked_sum[0] = data[0]
count = 0
_max = 0
for i in range(1,N):
    stacked_sum[i] = data[i] + stacked_sum[i-1]

if stacked_sum[X-1] != 0:
    _max = stacked_sum[X-1]
    count = 1


for i in range(X,N):
    if stacked_sum[i] - stacked_sum[i-X] > _max:
        _max = stacked_sum[i] - stacked_sum[i-X]
        count =1
    elif stacked_sum[i]-stacked_sum[i-X] == _max:
        count +=1

if N == 1:
    print(data[0])
    print(1)
elif _max != 0:
    print(_max)
    print(count)
else:
    print('SAD')


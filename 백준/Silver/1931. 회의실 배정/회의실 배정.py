import sys
input = sys.stdin.readline

N = int(input())

room_info = [list(map(int,input().split())) for _ in range(N)]


room_info.sort(key= lambda x:(x[0],x[1]))

count = 1
big = 10284701248749128478927
for i in range(N):
    if room_info[i][0] >= big:
        count +=1
        big = room_info[i][1]
    if room_info[i][1] <= big:
        big = room_info[i][1]


print(count)
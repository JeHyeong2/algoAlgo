# 꽃 앞에 시작월 11전 월이 끝나는게 12 이면 ok
import sys
input = sys.stdin.readline
N = int(input())

roses = [list(map(int,input().split())) for _ in range(N)]

roses.sort(key= lambda x:(x[0],x[1],x[2],x[3]))
over_3 = False
over_11 = False
connect = True
_min = [0,0]
_max = [0,0]
count = 0
idx = 0

for i in range(idx,len(roses)):
    if not connect:
        break
    m1, d1 , m2 , d2 = roses[i]

    if m1 < 3 <= m2 or (m1 == 3 and d1 == 1):
        over_3 = True
        if m2 > _max[0] or (m2 == _max[0] and d2 > _max[1]):
            _min[0],_min[1] = m1, d1
            _max[0], _max[1] = m2, d2
        count = 1
        idx = i+1
        if m2 == 12:
            connect = True
            over_11 = True
            break
        continue
    if m1 >= 3 and not over_3:
        break
    tmp_min = [0,0]
    tmp_max = [0,0]
    tmp_idx = 0
    for j in range(idx,len(roses)):
        m1, d1 , m2 , d2 = roses[j]
        if m1 < _max[0] or (m1 == _max[0] and d1 <= _max[1]):
            if tmp_max[0] < m2:
                tmp_max[0], tmp_max[1] = m2, d2
                tmp_idx = j
                tmp_min[0], tmp_min[1] = m1,d1
            elif tmp_max[0] == m2 and tmp_max[1] < d2:
                tmp_max[0], tmp_max[1] = m2, d2
                tmp_idx = j
                tmp_min[0], tmp_min[1] = m1, d1
        else:
            break
    if tmp_max[0] ==12:
        over_11 = True
        count +=1
        break
    if sum(tmp_max)==0:
        connect = False
        break
    count += 1
    _min = tmp_min
    _max = tmp_max
    idx = tmp_idx+1





if over_3 and over_11 and connect:
    print(count)
else:
    print(0)
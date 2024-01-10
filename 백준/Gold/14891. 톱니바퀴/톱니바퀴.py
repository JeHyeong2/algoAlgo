from collections import deque

def circling(S,C,H):
    Q = deque()
    Q.append(S)
    while Q:
        i = Q.pop()
        # 반시계 -1 , 시계 1
        # 시계일 경우 오른쪽 pop, appendleft , 반시계일 경우 popleft , append
        # N = 0 , S = 1
        H[i[0]] = 1
        # 돌았는지 안돌았는지 표시

        if i[1] == -1:
            change = C[i[0]].popleft()
            C[i[0]].append(change)
        if i[1] == 1:
            change = C[i[0]].pop()
            C[i[0]].appendleft(change)

        if i[0] < 4:
            if H[i[0]+1] != 1:
                if i[1] == 1:
                    if C[i[0]][3] != C[i[0]+1][6]:
                        Q.append((i[0]+1,i[1] * -1))
                elif i[1] == -1:
                    if C[i[0]][1] != C[i[0]+1][6]:
                        Q.append((i[0]+1,i[1] * -1))
        if i[0] > 1:
            if H[i[0]-1] != 1:
                if i[1] == 1:
                    if C[i[0]][7] != C[i[0]-1][2]:
                        Q.append((i[0]-1, i[1] * -1))
                elif i[1] == -1:
                    if C[i[0]][5] != C[i[0]-1][2]:
                        Q.append((i[0]-1, i[1] * -1))
        # if i[0] == 1:
        #     if i[1] == -1:
        #         if H[i[0]+1] == 0 and C[i[0]][1] != C[i[0]+1][6]:
        #             Q.append((i[0]+1,i[1]*-1))
        #     if i[1] == 1:
        #         if H[i[0]+1] == 0 and C[i[0]][3] != C[i[0]+1][6]:
        #             Q.append((i[0]+1,i[1]*-1))
        #     else:
        #         continue
        # elif i[0] == 4:
        #     if i[1] == 1:
        #         if H[i[0] - 1] == 0 and C[i[0]][7] != C[i[0] - 1][2]:
        #             Q.append((i[0] - 1, i[1] * -1))
        #         else:
        #             continue
        #     if i[1] == -1:
        #         if H[i[0] - 1] == 0 and C[i[0]][5] != C[i[0] - 1][2]:
        #             Q.append((i[0] - 1, i[1] * -1))
        #         else:
        #             continue
        # else:
        #     if H[i[0]+1] == 0:
        #         if i[1] == 1:
        #             if C[i[0]][3] != C[i[0] + 1][6]:
        #                 Q.append((i[0] + 1, i[1] * -1))
        #         else:
        #             if C[i[0]][1] != C[i[0] + 1][6]:
        #                 Q.append((i[0] + 1, i[1] * -1))
        #     if H[i[0]-1] == 0:
        #         if i[1] == 1:
        #             if C[i[0]][7] != C[i[0] - 1][2]:
        #                 Q.append((i[0] + 1, i[1] * -1))
        #         else:
        #             if C[i[0]][5] != C[i[0] - 1][2]:
        #                 Q.append((i[0] + 1, i[1] * -1))
        #

    return C


circle_ = [list(map(int,input())) for _ in range(4)]
circle = [[]]

for i in circle_:
    circle.append(deque(i))

had = [0]*5
k = int(input())
spin = []

for _ in range(k):
    spin.append(list(map(int,input().split())))

for i in spin:
    circle = circling(i,circle,had)
    had = [0]*5

point = 0
for n,i in enumerate(circle):
    if n == 0:
        continue
    if i[0] == 1:
        if n == 1:
            point += 1
        if n == 2:
            point += 2
        if n == 3:
            point += 4
        if n == 4:
            point += 8

print(point)
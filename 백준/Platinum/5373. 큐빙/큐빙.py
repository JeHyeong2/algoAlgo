from collections import deque
from copy import deepcopy
def spining_single(arr,dir,count):
    emt = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            emt[i][j] = arr[i][j]

    if dir == "+":
        for i in range(count):
            top, bot = [], []
            left, right = [],[]
            for j in range(3):
                top.append(emt[2-j][0])
                bot.append(emt[2-j][2])
                right.append(emt[0][j])
                left.append(emt[2][j])
            for j in range(3):
                emt[j][0] = left[j]
                emt[j][2] = right[j]
            emt[0] = top
            emt[2] = bot
    if dir == "-":
        for i in range(count):
            top, bot = [], []
            left, right = [], []
            for j in range(3):
                top.append(emt[j][2])
                bot.append(emt[j][0])
                left.append(emt[0][2-j])
                right.append(emt[2][2-j])
            for j in range(3):
                emt[j][0] = left[j]
                emt[j][2] = right[j]
            emt[0] = top
            emt[2] = bot
    return emt

# def mirroring(origin):
#     mirror = deepcopy(origin)
#     left = []
#     right = []
#
#     for i in range(3):
#         right.append(origin[i][0])
#         left.append(origin[i][2])
#     for i in range(3):
#         mirror[i][0] = left[i]
#         mirror[i][2] = right[i]
#     print(mirror)

def spining_double(side,dir):
    # back,top,front,bottom

    sidenum_list = {"B": 1, "U": 2, "F": 3, "D": 4}
    sidenum = sidenum_list[side]
    cube_side[sidenum] = spining_single(cube_side[sidenum], dir, 1)

    top_side = deepcopy(cube_side[sidenum - 1][2])
    bottom_side = deepcopy(cube_side[sidenum + 1][0])
    right_side = []
    left_side = []


    for i in range(3):
        left_side.append(L[i][2])
        right_side.append(R[i][0])


    # if side == "L":
    # if side == "R":
    if dir =="+":
        for i in range(3):
            cube_side[sidenum -1][2][i] = left_side[2-i]
            cube_side[sidenum+1][0][i] = right_side[2-i]
            R[i][0] = top_side[i]
            L[i][2] = bottom_side[i]

    if dir =="-":
        for i in range(3):
            cube_side[sidenum - 1][2][i] = right_side[i]
            cube_side[sidenum + 1][0][i] = left_side[i]
            R[i][0] = bottom_side[2-i]
            L[i][2] = top_side[2-i]

    if side == "B":
        cube_side[4] = cube_side[0]
    if side == "D":
        cube_side[1] = cube_side[5]


def side_spining(side,dir):

        # back , top , front ,bottom
        one_side = []
        two_side = []
        three_side = []
        four_side =[]
        if side == "L":
            for i in range(3):
                one_side.append(cube_side[1][i][0])
                two_side.append(cube_side[2][i][0])
                three_side.append(cube_side[3][i][0])
                four_side.append(cube_side[4][i][0])
            if dir == "+":
                for i in range(3):
                    cube_side[1][i][0] = four_side[i]
                    cube_side[2][i][0] = one_side[i]
                    cube_side[3][i][0] = two_side[i]
                    cube_side[4][i][0] = three_side[i]
            if dir == "-":
                for i in range(3):
                    cube_side[1][i][0] = two_side[i]
                    cube_side[2][i][0] = three_side[i]
                    cube_side[3][i][0] = four_side[i]
                    cube_side[4][i][0] = one_side[i]
        if side == "R":
            for i in range(3):
                one_side.append(cube_side[1][i][2])
                two_side.append(cube_side[2][i][2])
                three_side.append(cube_side[3][i][2])
                four_side.append(cube_side[4][i][2])
            if dir == "+":
                for i in range(3):
                    cube_side[1][i][2] = two_side[i]
                    cube_side[2][i][2] = three_side[i]
                    cube_side[3][i][2] = four_side[i]
                    cube_side[4][i][2] = one_side[i]
            if dir == "-":
                for i in range(3):
                    cube_side[1][i][2] = four_side[i]
                    cube_side[2][i][2] = one_side[i]
                    cube_side[3][i][2] = two_side[i]
                    cube_side[4][i][2] = three_side[i]


T = int(input())

for tc in range(T):
    N = int(input())
    spin = list(map(str,input().split()))

    back = [["o"]*3 for _ in range(3)]
    top = [["w"]*3 for _ in range(3)]
    front = [["r"]*3 for _ in range(3)]
    bottom = [["y"]*3 for _ in range(3)]
    back_to_bottom = []
    bottom_to_back = []
    center = [[],back,top,front,bottom,[]]

    L = [["g"]*3 for _ in range(3)]
    R = [["b"]*3 for _ in range(3)]

    cube_side = []
    for i in center:
        cube_side.append(i)


    lft = [("+",2),("+",1),("+",0),("+",3)]
    rgt = [("-",2),("-",1),("-",0),("-",3)]

    direction = {"B":0, "U":1,"F":2, "D":3}



    for side,dir in spin:

        cube_side[0] = cube_side[4]
        cube_side[5] = cube_side[1]
        if side != "L" and side != "R":
            edge = direction[side]
            la, lb = lft[edge]
            ra, rb = rgt[edge]
            L = spining_single(L,la, lb)
            R = spining_single(R,ra, rb)
            spining_double(side,dir)
            L = spining_single(L,ra,rb)
            R = spining_single(R,la,lb)

        else:
            if side == "L":
                L = spining_single(L, dir, 1)
                side_spining(side,dir)
            else:
                R = spining_single(R, dir, 1)
                side_spining(side, dir)
    for i in cube_side[2]:
        print("".join(i))

    # for i in cube_side[2]:
    #     print(*i)




    # 앞일때 left right 원본 배열
    # 뒤 위 앞 밑

import sys

input = sys.stdin.readline






for tc in range(3):
    N = int(input())
    coin_list = []
    _sum = 0
    for _ in range(N):
        coin, coin_num = map(int,input().split())
        _sum += coin_num * coin
        coin_list.append([coin,coin_num])
    check1 = _sum%2
    if check1:
        print(0)
        continue
    goal = _sum//2
    coin_list.sort(key=lambda x:-x[0])
    cando = False
    checklist = [1] + [0]*goal
    for i in range(len(coin_list)):
        coin, coin_num = coin_list[i]
        for j in range(goal,coin-1,-1):
            if checklist[j - coin]:
                tmp = j - coin
                for k in range(1,coin_num+1):
                    if tmp + coin * k <= goal:
                        checklist[tmp+(coin*k)] = 1
                    else:
                        break
        if checklist[-1]:
            print(1)
            break
    else:
        print(0)
from copy import deepcopy

N = int(input())

needs = list(map(int,input().split()))

account = int(input())

ans = 0
avg = account // N

if sum(needs) <= account:
    ans = max(needs)
    print(ans)
else:
    before = 0
    after_num = 0
    needs.sort()

    for i in range(after_num,N):
        if needs[i] > avg:
            after_num = i
            break
        else:
            before += needs[i]
    high = avg
    while True:
        if before + high*len(needs[after_num:]) > account:
            print(high-1)
            break
        elif before + high*len(needs[after_num:]) == account:
            print(high)
            break
        else:
            high+=1
            for i in range(after_num, N):
                if needs[i] > high:
                    after_num = i
                    break
                else:
                    before += needs[i]

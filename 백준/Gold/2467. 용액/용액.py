def twopoint():
    done = False
    start = 0
    end = N-1
    _min = 2000000001
    ans_1 = 0
    ans_2 = 0

    while start != end:
        tmp = 0
        now = abs(lacture[start] + lacture[end])

        if now < abs(_min):
            _min = lacture[start] + lacture[end]
            ans_1 = lacture[start]
            ans_2 = lacture[end]
            tmp = end - 1
            if abs(lacture[start] + lacture[tmp]) < abs(_min):
                end = tmp
            else:
                start +=1
        else:
            if abs(lacture[start] + lacture[end-1]) < now:
                end -=1
            else:
                start+=1



    print(ans_1,ans_2)












N = int(input())

lacture = list(map(int,input().split()))

lacture.sort()


twopoint()
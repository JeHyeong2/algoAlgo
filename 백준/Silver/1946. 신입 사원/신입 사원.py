T = int(input())
for tc in range(T):
    N = int(input())
    man = []
    for _ in range(N):
        man.append(list(map(int,input().split())))
    man.sort(key= lambda x:x[0])
    count = len(man)
    falling = []
    for i in range(len(man)-1,-1,-1):
        falling.append((man[i][1],i))
    a = sorted(falling,key=lambda x:x)
    high = 10928374635
    for i in range(len(a)):
        if a[i][1] < high:
            high = a[i][1]
        if a[i][1] > high:
            count -= 1


    print(count)
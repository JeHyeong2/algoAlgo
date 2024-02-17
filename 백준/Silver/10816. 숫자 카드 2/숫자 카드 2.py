def findcard(i):
    start = 0
    end = len(sangka) - 1
    founded = False
    first = 0
    second =0
    while start <= end:
        mid =(start+end) //2
        if sangka[mid] == i:
            end = mid-1
            founded = True
        elif sangka[mid] < i:
            start = mid + 1
        else:
            end = mid -1
    if founded:
        first = start
        start2 = start
        end = len(sangka)-1
        while start2 <= end:
            mid = (start2 + end) // 2
            if sangka[mid] == i:
                start2 = mid + 1
            if sangka[mid] < i:
                start2 = mid + 1
            if sangka[mid] > i:
                end = mid -1
        second = start2-1
        return second - first + 1
    else:
        return 0



N = int(input())

sangka = list(map(int,input().split()))

M = int(input())

findka = list(map(int,input().split()))

sangka.sort()


ans = []
for i in findka:
    a = findcard(i)
    ans.append(a)

print(*ans)
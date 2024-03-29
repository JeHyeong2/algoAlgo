import sys
input = sys.stdin.readline

def makelist(n):
    if n >=3:
        for i in range(3,n+1):
            zerolist[i] = zerolist[i-1]+zerolist[i-2]
            onelist[i] = onelist[i-1]+onelist[i-2]
    else:
        return
N = int(input())



inputlist = []
for i in range(N):
    a= int(input())
    inputlist.append(a)

for i in inputlist:
    zerolist = [0] * (40 + 1)
    onelist = [0] * (40 + 1)
    zerolist[0] = 1
    onelist[1] = 1
    zerolist[2] = 1
    onelist[2] = 1
    makelist(i)
    print(zerolist[i],onelist[i])
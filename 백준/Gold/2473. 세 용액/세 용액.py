import sys
input = sys.stdin.readline
N = int(input())

lab = list(map(int,input().split()))

lab.sort()
s1 = s2 = s3 = 0
ans = 3000000000
for i in range(N-2):
    start = i+1
    end = N-1
    while start < end:
        dragon_water = lab[i] + lab[start] + lab[end]
        if abs(dragon_water) < ans:
            ans = abs(dragon_water)
            s1,s2,s3 = lab[i],lab[start],lab[end]
        if dragon_water < 0:
            start +=1
        else:
            end -=1




print(s1,s2,s3)
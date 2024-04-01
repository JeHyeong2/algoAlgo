import sys
input = sys.stdin.readline

def find_N():
    large_num = []


    for i in range(N):
        large_num.append((table[N-1][i],N-1,i))

    count = N
    ans = 0
    while count:
        large_num.sort()
        num,s1,s2 = large_num.pop()
        ans = num
        count -= 1
        if 0<= s1 <=N and 0<= s2 <=N:
            large_num.append((table[s1-1][s2],s1-1,s2))
    print(ans)





INF = -1000000001

N = int(input())

table = [list(map(int,input().split())) for _ in range(N)]

find_N()
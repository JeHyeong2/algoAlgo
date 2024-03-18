import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    a, b = map(int,input().split())

    ans = []
    for i in range(1,b+1):
        tmp = str(a**i)
        if tmp[-1] not in ans:
            ans.append(tmp[-1])
        else:
            break
    if a%10 == 0:
        print(10)
    elif len(ans) == 1:
        print(ans[0])
    else:
        print(ans[(b%len(ans))-1])


N = int(input())


ans = 0

plus = []
minus = []
numlist = [int(input()) for _ in range(N)]

numlist.sort()
for i in numlist:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)
minus.sort(reverse=True)

if plus:
    while plus:
        a = plus.pop()
        if plus:
            b = plus.pop()
            if b == 1:
                ans += a
                ans +=b
                continue
            ans += a*b
        else:
            ans += a
if minus:
    while minus:
        a = minus.pop()
        if minus:
            b = minus.pop()
            ans += a * b
        else:
            ans += a
print(ans)




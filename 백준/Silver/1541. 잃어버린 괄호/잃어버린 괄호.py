number = input()

a = number.split("-")

ans = 0
num = []

for i in a:
    b = i.lstrip("0")
    num.append(b)

for n,i in enumerate(num):
    if "+" in i:
        tmp = 0
        b = i.split("+")
        for j in b:
            tmp += int(j)
        if n == 0:
            ans += tmp
        else:
            ans -= tmp
    else:
        if n == 0:
            ans += int(i)
        else:
            ans -= int(i)

print(ans)
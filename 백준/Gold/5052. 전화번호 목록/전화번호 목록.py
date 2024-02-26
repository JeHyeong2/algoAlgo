T = int(input())

for tc in range(T):
    N = int(input())
    phonenumber = [[] for _ in range(11)]
    num = []
    for _ in range(N):
        nb = (input())
        num.append(nb)
        phonenumber[len(nb)].append(nb)
    Check = False
    for i in num:
        a = len(i)
        for j in range(1,a):
            b = i[:j]
            if b in phonenumber[j]:
                Check = True

    if Check == True:
        print("NO")
    else:
        print("YES")



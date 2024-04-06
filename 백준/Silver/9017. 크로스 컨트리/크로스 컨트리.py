import sys

input = sys.stdin.readline
T = int(input())

for tc in range(T):
    N = int(input())
    first = [0]*N
    check = list(map(int,input().split()))
    team = {}

    for i in range(N):
        first[i] = check[i]
        if check[i] not in team:
            team[check[i]] = [i+1]
        else:
            team[check[i]].append(i+1)

    out = []

    for tn,gr in team.items():
        if len(gr) < 6:
           out.append(tn)

    medal = []

    for i in range(len(first)):
        if first[i] not in out:
            medal.append(first[i])

    anslist = [[] for _ in range(max(medal)+1)]
    num5 = [0] * (max(medal)+1)


    for i in range(len(medal)):
        if len(anslist[medal[i]]) < 4:
            anslist[medal[i]].append(i+1)
        else:
            if not num5[medal[i]]:
                num5[medal[i]] = i+1

    _min = 8174987
    ans = 0
    for n,i in enumerate(anslist):
        if i:
            if sum(i) < _min:
                _min = sum(i)
                ans = n
            if sum(i) == _min:
                if num5[ans] > num5[n]:
                    ans = n

    print(ans)
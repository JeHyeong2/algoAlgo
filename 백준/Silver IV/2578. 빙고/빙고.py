def checkline():
    global ans
    crossr = 0
    crossl = 0
    for i in range(5):
        if bingo[i][i] == 0:
            crossr += 1
        if bingo[abs(i - 4)][i] == 0:
            crossl += 1
    if crossl == 5:
        ans += 1
    if crossr == 5:
        ans += 1
    for i in range(5):
        x = 0
        y = 0
        for j in range(5):
            if bingo[i][j] == 0:
                x += 1
            if bingo[j][i] == 0:
                y += 1
        if x == 5:
            ans += 1
        if y == 5:
            ans += 1


def playbingo(n):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == n:
                bingo[i][j] = 0
                return

bingo = []
call = []
ans = 0

for _ in range(5):
    line = list(map(int,input().split()))
    bingo.append(line)
for _ in range(5):
    call_line = list(map(int,input().split()))
    call.append(call_line)

count = 0
total_ans =0
for i in call:
    for j in i:
        playbingo(j)
        checkline()
        count+=1
        if ans >= 3 and total_ans == 0:
            total_ans = count
        else:
            ans = 0
print(total_ans)

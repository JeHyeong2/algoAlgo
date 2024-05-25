import sys
input = sys.stdin.readline
N, M = map(int,input().split())


lst = []


for i in range(N):
    a = int(input())
    lst.append(a)
ans = 0


checker = [[0]*(M+1) for _ in range(len(lst))]
if lst[0] == 1:
    checker[0][0] = 1
else:
    checker[0][1] = 1

for i in range(1,N):

    if i + 1 < M:
        if lst[i] == 1:
            for j in range(2,i+2,2):
                if checker[i-1][j-1] +1 > checker[i-1][j] +1 :
                    checker [i][j] = checker[i-1][j-1] +1
                else:
                    checker[i][j] = checker[i-1][j] +1
            for j in range(1,i+2,2):
                if checker[i-1][j-1] > checker[i-1][j]:
                    checker[i][j] = checker[i-1][j-1]
                else:
                    checker[i][j] = checker[i-1][j]
        else:
            for j in range(2,i+2,2):
                if checker[i-1][j-1] > checker[i-1][j]:
                    checker [i][j] = checker[i-1][j-1]
                else:
                    checker[i][j] = checker[i-1][j]
            for j in range(1,i+2,2):
                if checker[i-1][j-1] +1 > checker[i-1][j] +1:
                    checker[i][j] = checker[i-1][j-1] +1
                else:
                    checker[i][j] = checker[i-1][j] + 1
    else:
        if lst[i] == 1:
            for j in range(2,M+1,2):
                if checker[i-1][j-1] +1 > checker[i-1][j] +1 :
                    checker [i][j] = checker[i-1][j-1] +1
                else:
                    checker[i][j] = checker[i-1][j] +1
            for j in range(1,M+1,2):
                if checker[i-1][j-1] > checker[i-1][j]:
                    checker[i][j] = checker[i-1][j-1]
                else:
                    checker[i][j] = checker[i-1][j]
        else:
            for j in range(2,M+1,2):
                if checker[i-1][j-1] > checker[i-1][j]:
                    checker [i][j] = checker[i-1][j-1]
                else:
                    checker[i][j] = checker[i-1][j]
            for j in range(1,M+1,2):
                if checker[i-1][j-1] +1 > checker[i-1][j] +1:
                    checker[i][j] = checker[i-1][j-1] +1
                else:
                    checker[i][j] = checker[i-1][j] + 1
    if lst[i] == 1:
        checker[i][0] = checker[i-1][0] + 1
    else:
        checker[i][0] = checker[i-1][0]
print(max(checker[-1]))
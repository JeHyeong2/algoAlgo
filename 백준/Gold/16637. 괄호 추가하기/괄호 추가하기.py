from copy import deepcopy
from collections import deque
import sys
sys.setrecursionlimit(10000)

def plus(a,b):
    return int(a)+int(b)

def multiple(a,b):
    return int(a)*int(b)

def minus(a,b):
    return int(a) - int(b)

def dfs(s,vs):
    global _max
    v = deepcopy(vs)
    usedNum = [False] * N
    ans = deque()
    now = 0
    for i in range(N):
        if not pp[i].isnumeric():
            if v[now]:
                if pp[i] == "+":
                    ans.append(plus(pp[i-1],pp[i+1]))
                    usedNum[i-1] = True
                    usedNum[i] = True
                    usedNum[i+1] = True
                elif pp[i] == "-":
                    ans.append(minus(pp[i-1],pp[i+1]))
                    usedNum[i - 1] = True
                    usedNum[i] = True
                    usedNum[i + 1] = True
                else:
                    ans.append(multiple(pp[i-1],pp[i+1]))
                    usedNum[i - 1] = True
                    usedNum[i] = True
                    usedNum[i + 1] = True
            now +=1
    now = 0
    jump = False
    answer = []

    for i in range(N):
        if not usedNum[i]:
            answer.append(pp[i])
            jump = False
        else:
            if not jump:
                answer.append(ans.popleft())
                jump = True
    _sum = 0
    nn = [False] * len(answer)
    for i in range(len(answer)):
        if not nn[i]:
            if i == 0 :
                nn[i] = True
                _sum = int(answer[i])
            if not pp[i].isnumeric():
                if answer[i] == "+":
                    _sum = (plus(_sum, answer[i + 1]))
                    nn[i] = True
                    nn[i+1] = True
                elif answer[i] == "-":
                    _sum = (minus(_sum, answer[i + 1]))
                    nn[i] = True
                    nn[i+1] = True
                else:
                    _sum = (multiple(_sum, answer[i + 1]))
                    nn[i] = True
                    nn[i+1] = True

    if _max < _sum:
        _max = _sum

    for i in range(s,len(v)):
        if i > 0:
            if not v[i] and not v[i-1]:
                v[i] = True
                dfs(i,v)
                v[i] = False
        else:
            if not v[i]:
                v[i] = True
                dfs(i,v)
                v[i] = False

    return


N = int(input())

pp = list(input())
_max = -2**31
visited = [False] * (N//2)

dfs(0,visited)
print(_max)


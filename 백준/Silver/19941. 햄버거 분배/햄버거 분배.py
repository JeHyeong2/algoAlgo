from collections import deque
import sys
input = sys.stdin.readline

N , M = map(int,input().split())


table = list(input())
hamberger = deque()
human = deque()
for n,i in enumerate(table):
    if i == "H":
        hamberger.append(n)
    if i == "P":
        human.append(n)
count = 0

man = 0
burger = 0
if hamberger and human:
    while True:
        if man == 0 and burger == 0:
            man = human.popleft()
            burger = hamberger.popleft()
        if burger - M <= man <= burger + M:
            count += 1
            if human and hamberger:
                man = human.popleft()
                burger = hamberger.popleft()
            else:
                break
        else:
            if burger > man:
                if human:
                    man = human.popleft()
                else:
                    break
            else:
                if hamberger:
                    burger = hamberger.popleft()
                else:
                    break



print(count)

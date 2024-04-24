from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())

first = {}
word_list =[]
fpoint = 0
for i in range(N):
    word = input().strip()
    if i == 0:
        for j in word:
            fpoint += 1
            if j not in first:
                first[j] = 1
            else:
                first[j] +=1
    else:
        word_list.append(word)

ans = 0
for word in word_list:
    firstpoint = fpoint
    point = len(word)
    fword = deepcopy(first)
    for j in word:
        if j not in fword:
            continue
        if fword[j]:
            fword[j] -= 1
            point -= 1
            firstpoint -=1
    if -1 <= point <= 1 and -1 <= firstpoint <= 1 :
        ans +=1
print(ans)

import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

# L: 커서 왼쪽으로 한칸 ( 0 이면 무시 )
# D : 커서 오른쪽으로 한칸( -1 이면 무시)
# B : 커서 왼쪽에 있는 문자삭제 (맨앞이면 무시)
# P : 문사를 커서 왼쪽에 추가

word = list(input())
cursor_right = deque()
N = int(input())
cursor = len(word)
# for _ in range(N):
#     a = list(input().split())
#     if a[0] == "P":
#         word.insert(cursor, a[1])
#         cursor += 1
#     elif a[0] == "L":
#         if cursor > 0:
#             cursor -= 1
#     elif a[0] == "D":
#         if cursor < N:
#             cursor +=1
#     else:
#         if cursor > 0:
#             word.pop(cursor-1)
#             cursor -=1
for _ in range(N):
    a = list(input().split())
    if a[0] == "P":
        word.append(a[1])
        cursor +=1
    elif a[0] == "L":
        if cursor > 0:
            b = word.pop()
            cursor_right.appendleft(b)
            cursor -=1
    elif a[0] == "D":
        if cursor < N:
            if cursor_right:
                b = cursor_right.popleft()
                word.append(b)
                cursor+=1
    else:
        if cursor > 0:
            word.pop()
            cursor -=1
a1 = "".join(word)
a2 = "".join(cursor_right)
ans = a1+a2
print(ans)
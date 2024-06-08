import sys
input = sys.stdin.readline
def case_a(n1,n2):
    global usa
    while n1 < n2:

        if l[n1] == l[n2]:
            n1+=1
            n2-=1
        else:
            return False
    usa = True
    return

def case_b(n1,n2):
    global usa

    while n1 < n2:
        if l[n1] == l[n2]:
            n1+=1
            n2-=1
        else:
            return False
    usa = True
    return

N = int(input())

for _ in range(N):
    l = list(input().strip())
    usa = False
    moon = False
    lft = 0
    rgt = (len(l)-1)
    while lft < rgt:
        if l[lft] == l[rgt]:
            lft += 1
            rgt -= 1
        else:
            case_a(lft,rgt-1)
            case_b(lft+1,rgt)
            break
    else:
        moon = True

    if moon:
        print(0)
    elif usa:
        print(1)
    else:
        print(2)
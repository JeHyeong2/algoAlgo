import heapq
N = int(input())

tower = list(map(int,input().split()))

nlist = []
anslist = [0]*N
h = []
heapq.heapify(h)

for i in range(N-1,-1,-1):
    nlist.append((tower[i],i))

for i in nlist:
    if not h:
        heapq.heappush(h,i)
    elif h[0][0] < i[0]:
        if h:
            while i[0] > h[0][0]:
                a,b = heapq.heappop(h)
                anslist[b] = i[1]+1
                if not h:
                    break
            heapq.heappush(h,i)
    else:
        heapq.heappush(h,i)
print(*anslist)

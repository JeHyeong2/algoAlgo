import heapq

def solution(operations):
    h = [] 
    
    for i in operations:
        inp = i.split()
        if inp[0] == "I":
            heapq.heappush(h,int(inp[1]))
        else:
            if len(h) == 0:
                continue
            if i == "D 1":
                h.sort()
                h.pop()
            else:
                heapq.heappop(h)
    h.sort()
    if len(h) == 0 :
        return [0,0]
    else:
        return [h[-1],h[0]]
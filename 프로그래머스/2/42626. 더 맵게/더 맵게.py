import heapq

def solution(scoville, K):
    answer = 0
    h = scoville
    heapq.heapify(h)
  
    while h[0] < K:
        if len(h)>1:
            food1 = heapq.heappop(h)
            food2 = heapq.heappop(h)
            new_food = food1 + (food2*2)
            heapq.heappush(h,new_food)
            answer+=1
        else:
            return -1
    
    return answer
from collections import deque

def solution(numbers, target):
    
    answer = 0
    length = len(numbers)
    

    def make_deal():
        ans = 0
        q = [(0,0)] 
        
        while q:
            now,_sum = q.pop()
            if now == length:
                if _sum == target:
                    ans +=1
                    continue
                else:
                    continue
            
            plus = _sum + numbers[now] 
            minus = _sum + -numbers[now]
            q.append((now+1, plus))
            q.append((now+1, minus))
            
        return ans
   

    
    return make_deal()
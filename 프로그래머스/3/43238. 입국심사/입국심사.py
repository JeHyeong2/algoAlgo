def solution(n, times):
    # n 명 입국심사
    # 심사관이 걸리는 시간 times 
    start , end = 1, max(times)*n
    ans = 0
    
    while start < end:
        mid = (start + end) // 2
        
        count = 0
        for i in times:
            count += mid//i
        
        
        if count >= n:
            end = mid
        else:
            start = mid + 1
        ans = start
            
            
            
    
    return ans
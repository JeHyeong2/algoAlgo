def solution(n, times):
    ans = 0
    
    start , end = 1, max(times) * n
    
    while start < end:
        mid = (start+end) // 2 
        people = 0
        
        for time in times:
            people += (mid//time)
        
        if people >= n:
            end = mid
        else:
            start = mid + 1 
    
    
    return start
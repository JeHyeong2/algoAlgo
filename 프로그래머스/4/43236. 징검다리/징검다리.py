def solution(distance, rocks, n):
    rocks = sorted(rocks) + [distance]
    start,end = 1, distance
    # m 이상의 거리를 유지하며 바위를 n 개 제거할 수 있는가?
    
    while start <= end:
    
        m = (start + end) //2
        now = 0
        broke = 0
        for i in range(len(rocks)):
            if rocks[i] - now < m:
                broke += 1
            else:
                now = rocks[i]
        if broke > n:
            end = m - 1
        else:
            answer = m
            start = m + 1 

    
    
    return answer
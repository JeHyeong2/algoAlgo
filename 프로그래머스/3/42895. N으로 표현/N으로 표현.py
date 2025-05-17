def solution(N, number):
    answer = 0
    
    if N == number:
        return 1
    
    S = [set() for _ in range(9)]
    
    
    for i in range(1,9):
        S[i].add(int(str(N)*i))
        for j in range(1,i):
            for a in S[j]:
                for b in S[i-j]:
                    S[i].add(a+b)
                    S[i].add(a-b)
                    S[i].add(a*b)
                    if b != 0:
                        S[i].add(a//b)
        if number in S[i]:
            return i
    else:
        return -1
                    
    
    
    
    return answer
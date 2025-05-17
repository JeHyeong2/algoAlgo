def solution(clothes):
    answer = 0
    
    closet = {}
    
    for i in clothes:
        if i[1] not in closet:
            closet[i[1]] = [i[0]]
        else:
            closet[i[1]].append(i[0])
    
    
    num = []
    for i in closet.keys():
        num.append(len(closet[i]))
    
    result = 1
    for i in num:
        result *= (i+1)
    
    result -=1
    
        
    return result
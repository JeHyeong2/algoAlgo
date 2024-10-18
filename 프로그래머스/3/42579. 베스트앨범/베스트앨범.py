def solution(genres, plays):
    answer = []
    
    pl = {}
    
    for i in range(len(genres)):
        if genres[i] not in pl:
            pl[genres[i]] = [plays[i],[(plays[i],i)]]
        else:
            pl[genres[i]][0] += plays[i]
            pl[genres[i]][1].append((plays[i],i))
    
    sorted_pl = sorted(pl.items(), reverse = True , key = lambda x:x[1][0])

    for k,v in sorted_pl:
        sorted_v = sorted(v[1], reverse = True,key= lambda x:x[0])
        for i in range(len(sorted_v)):
            answer.append(sorted_v[i][1])
            if i == 1:
                break
    
    return answer
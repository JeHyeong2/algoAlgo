import copy
def solution(k, dungeons):
    answer = -1
    
    # k 는 현재 피로도
    # 최소필요 피로도, 소모피로도
    visited = [0] * len(dungeons)
    ans = 0
    def game(hp,visited,c):
        nonlocal ans
        v = copy.copy(visited)
        if sum(v) == len(dungeons):
            if c > ans:
                ans = c
            return
        for i in range(len(dungeons)):
            if v[i] == 0:
                v[i] = 1
                if hp >= dungeons[i][0]:
                    game(hp-dungeons[i][1],v,c+1)
                else:
                    game(hp,v,c)
                v[i] = 0
    
    game(k,visited,0)
    
                
                
    
    return ans
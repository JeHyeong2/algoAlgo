from collections import deque 
def solution(n, edge):
    answer = 0
    
    edge_info = {}
    
    for i in edge:
        if i[0] not in edge_info:
            edge_info[i[0]] = [i[1]]
        else:
            edge_info[i[0]].append(i[1])
        if i[1] not in edge_info:
            edge_info[i[1]] = [i[0]]
        else:
            edge_info[i[1]].append(i[0])
            
    
    weight = [-1]*(n+1)
    weight[1] = 0 
    dq = deque()
    dq.append(1)
    
    while dq:
        node = dq.popleft()
        
        for next_node in edge_info[node]:
            if weight[next_node] == -1:
                weight[next_node] = weight[node] + 1
                dq.append((next_node))
            else:
                continue
    
    return weight.count(max(weight))
        
    
    
    return answer
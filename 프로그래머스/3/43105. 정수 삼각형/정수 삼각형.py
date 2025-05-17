import copy
def solution(triangle):
    answer = 0
    
    t_g_last = [0 for _ in range(len(triangle))]
    t_g_now = [0 for _ in range(len(triangle))]
    
    t_g_last[0] = triangle[0][0]
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                t_g_now[j] = triangle[i][j] + t_g_last[j] 
                
            elif j == len(triangle[i])-1:
                t_g_now[j] = triangle[i][j] + t_g_last[j-1]
                
            else:
                num1 = t_g_last[j] + triangle[i][j]
                num2 = t_g_last[j-1] + triangle[i][j]
                if num1 > num2:
                    t_g_now[j] = num1
                else:
                    t_g_now[j] = num2
        t_g_last = copy.deepcopy(t_g_now)
    
             
                
            
            
    return max(t_g_last)
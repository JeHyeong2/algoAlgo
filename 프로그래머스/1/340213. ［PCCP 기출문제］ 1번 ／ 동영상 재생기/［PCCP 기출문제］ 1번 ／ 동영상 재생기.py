def solution(video, now, op_start, op_end, commands):

    video_length = list(map(int,video.split(":")))
    
    endM = video_length[0]
    endS = video_length[1]
    
    now_info = list(map(int,now.split(":")))
    nowM = now_info[0]
    nowS = now_info[1]
    
    ops_info = list(map(int,op_start.split(":")))
    ope_info = list(map(int,op_end.split(":")))
    
    
    def check_op(nM,nS):
        time = [nM,nS]
        if nM > ope_info[0]:
            return time
        if nM < ops_info[0]:
            return time
        
        if nM == ops_info[0]:
            if nS < ops_info[1]:
                return time
        
        if nM == ope_info[0]:
            if nS > ope_info[1]:
                return time
        
        return ope_info 
    
    for i in commands:
        n = check_op(nowM,nowS)
        nowM = n[0]
        nowS = n[1]

        if i == "next":
            if nowS + 10 >= 60:
                nowM += 1
                nowS = (nowS + 10) % 60
                if nowM > endM:
                    nowM = endM
                    nowS = endS
            else: 
                nowS += 10
            if nowM == endM and nowS > endS:
                nowS = endS     
                    
        if i == "prev":
            if nowS - 10 < 0:
                if nowM == 0:
                    nowS = 0
                else:
                    nowM -= 1
                    nowS += 50
            else:
                nowS -= 10  
    
    final = check_op(nowM,nowS)
    if final[0] // 10 < 1:
        final[0] = f"0{final[0]}"
    else:
        final[0] = str(final[0])
    if final[1] // 10 < 1:
        final[1] = f"0{final[1]}"
    else:
        final[1] = str(final[1])
    
    answer = ":".join(final)
    
    
        

    
    #오프닝 구간 안쪽이면 오프닝 끝나는시간으로 
    #prev 10초 전으로 만약 10보다 작으면 0 
    #next 10초 뒤로 만약 동영상 길이보다 크면 동영상크기  
    #동영상 위치 "mm:ss" 형식 
    #분,초 가 한자리면 0붙혀서 두자리로
    return answer
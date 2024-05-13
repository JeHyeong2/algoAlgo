function solution(land) {
    const n = land.length;
    const m = land[0].length;
    const visited = new Array(n);
    const info = new Array(m).fill(0)
    let index = 1
    const di = [0,-1,0,1]
    const dj = [-1,0,1,0]
    
    //visited 배열생성
    for (let i = 0 ; i < n ; i++){
        visited[i] = new Array(m).fill(0);
    };
    
    
    
    const bfs = (st) => {
        const q = [st]
        let cost = 0
        // 해당 영역에서 얻을 수 있는 석유의 양
        let check = new Array(m).fill(false)
        // 해당 유전이 가로 몇번째 인덱스에 존재하는지 
        
        while( q.length >0 ){
            let dest = q.pop()
            let s1 = dest[0]
            let s2 = dest[1]
            if(!visited[s1][s2]){
              check[s2]= true
              visited[s1][s2] = index
              cost +=1
            //visited 체크  
            }else{
              continue
            }
    
            for (let i = 0 ; i < 4 ; i++){
                let ni = s1 + di[i]
                let nj = s2 + dj[i]
                //4방향 탐색
                if (0 <= ni && ni < n && 0 <= nj && nj < m && !visited[ni][nj]  && land[ni][nj] == 1){
                    q.push([ni,nj])
                }; 
            };
        };
        
        for(let i = 0 ; i < m ; i++){
            // 몇번째 인덱스에서 석유가 얼마나 채취되는지 추가해줌
            //각 유전마다 한번의 bfs 서칭만으로 하기위해 다음과 같이 로직구성
          if (check[i]){
            info[i]+=cost
          }
        }
        
        index +=1
        // 다음인덱스로
    };
    
    //bfs 실행
    for (let i = 0 ; i < n ; i++){
        for (let j = 0 ; j < m ; j++){
            if (land[i][j]==1 && visited[i][j] == 0){
              bfs([i,j])
            }
        };
    };
    

    //각 가로 인덱스에서 얼마나 많은 석유가 나는지 기록해놓은 info 배열에서 가장 큰 수를 정답으로 리턴.
    return Math.max(...info);
}

function solution(land) {
    const n = land.length;
    const m = land[0].length;
    const visited = new Array(n);
    const info = new Array(m).fill(0)
    let index = 1
    const di = [0,-1,0,1]
    const dj = [-1,0,1,0]
    
    
    for (let i = 0 ; i < n ; i++){
        visited[i] = new Array(m).fill(0);
    };
    
    
    const bfs = (st) => {
        const q = [st]
        let cost = 0
        let check = new Array(m).fill(false)
        while( q.length >0 ){
            let dest = q.pop()
            let s1 = dest[0]
            let s2 = dest[1]
            if(!visited[s1][s2]){
              check[s2]= true
              visited[s1][s2] = index
              cost +=1
            }else{
              continue
            }
    
            for (let i = 0 ; i < 4 ; i++){
                let ni = s1 + di[i]
                let nj = s2 + dj[i]
                if (0 <= ni && ni < n && 0 <= nj && nj < m && !visited[ni][nj]  && land[ni][nj] == 1){
                    q.push([ni,nj])
                }; 
            };
        };
        for(let i = 0 ; i < m ; i++){
          if (check[i]){
            info[i]+=cost
          }
        }
        index +=1
    };
    
    
    for (let i = 0 ; i < n ; i++){
        for (let j = 0 ; j < m ; j++){
            if (land[i][j]==1 && visited[i][j] == 0){
              bfs([i,j])
            }
        };
    };
    


    return Math.max(...info);
}

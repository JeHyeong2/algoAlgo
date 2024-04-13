function solution(edges) {
    let answer = [0,0,0,0];
    //정점, 도넛 , 막대 , 8자
    const tree = {}
    let _max = 0
    
    
    for(let i = 0 ; i < edges.length; i++){
        let node = edges[i]
        if(tree[node[0]]){
            tree[node[0]].push(node[1])
        }else{
            tree[node[0]] = [node[1]]
        }
        _max = Math.max(_max,node[0],node[1])
    }
    const used = [...new Array(_max+1)].map((e)=> e = 0)
    for(let i = 0 ; i < edges.length; i++){
        let node = edges[i]
        used[node[0]] = 1
        used[node[1]] = 1
    }
    used[0] = 1
    console.log(used)
  
  
    const visited1 = [...new Array(_max+1)].map((e)=> e = 0)
    visited1[0] = -1
    let top = 0
    const double = []
    const single = []
    
    for(let node in tree){
        if(tree[node].length >2){
            top = node
        }else if(tree[node].length == 2){
            double.push(node)
            visited1[tree[node][0]] = 1
            visited1[tree[node][1]] = 1
        }else{
            single.push(node)
            visited1[tree[node][0]] = 1
        }
    }
    
    
    if(!top){
    for(let i = 0 ; i < double.length; i++){
        if (!visited1[double[i]]){
            top = double[i]
            break
        }
    }   

    }
      
    answer[0] = Number(top)
    answer[3] = tree[top].length ==2 ? double.length - 1 : answer[3]+=double.length
    answer[2] = 0
   
  
  
    const visited2 = [...new Array(_max+1)].map((e)=> e = 0)
    visited2[top] = -1
    visited2[0] = -1
    for(let i = 0 ; i < edges.length; i++){
        let node = edges[i]
        if(node[0] != top){
            visited2[node[1]] +=1
        }
    }
    for(let i = 0 ; i< visited2.length; i++){
        if (visited2[i] == 0 && used[i]){
            answer[2] +=1
        }
    }
    
    answer[1] = tree[top].length - answer[2] - answer[3] 
    
    
    

     return answer;
    
    }
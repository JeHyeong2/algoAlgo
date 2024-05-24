function solution(k, n, reqs) {
    let answer = 0;
    const client = new Array(k+1).fill(0).map(()=>[])     
    
    
    const wasteCheck = (arr,man) => {
      let time = 0
      const table = new Array(man).fill(0).map(()=>0)
      let pointer = 0
      const f1 = () =>{
        table.shift()
        table.push(arr[pointer][0] + arr[pointer][1])
        pointer += 1
        table.sort((a,b)=>(a-b))
      }
      const f2 = ()=>{
        let tmp = table[0] - arr[pointer][0]  
        time += table[0] - arr[pointer][0]                 
        table.shift()
        table.push(arr[pointer][0] + arr[pointer][1]+ tmp)
         pointer += 1
         table.sort((a,b)=>a-b)
      }
      
      
     for (let i = 0 ; i < arr.length ; i++){
       table[0] <= arr[pointer][0] ? f1() : f2()
     }
    return time
      
     }
   
    
  
  for(let i = 0 ; i < reqs.length; i++){
      client[reqs[i][2]].push(reqs[i])
    }
  
  const mentoNum = new Array(k+1).fill(1)
  let mento = n - k
  while(mento){
    let idx = 0
    let _max = 0
    for(let i = 1; i < client.length; i++){
      const pre = wasteCheck(client[i],mentoNum[i])
      const plus =wasteCheck(client[i],(mentoNum[i]+1))
      if(pre - plus > _max){
        _max = pre - plus
        idx = i
      }
    }
    mentoNum[idx]+=1
    mento -=1
  }

  for(let i = 1; i < client.length; i ++){
    let anstime = wasteCheck(client[i],mentoNum[i])
    answer += anstime
  }


  
    return answer;
}

const readline = require("readline")

const rl = readline.createInterface({
  input : process.stdin,
  output : process.stdout
})
let inputCount = 0
let N = 0
let C = 0
let items = []

rl.on("line",(line)=>{
  if(inputCount === 0){
    let inp = line.trim().split(" ").map((el)=> Number(el))
    N = inp[0]
    C = inp[1]
  }else{
     let inp = line.trim().split(" ").map((el)=> Number(el))
     items = inp
    rl.close()
  }
  inputCount+=1
})

rl.on("close",()=>{
  const itemA = items.slice(0,parseInt(items.length/2))
const itemB = items.slice(parseInt(items.length/2),items.length)

const sumA = []
const sumB = []
const visitedA = new Array(itemA.length).fill(false)
const visitedB = new Array(itemA.length).fill(false)
let ans = 1
const sumMaker = (alphabet,s,start) =>{
  let arr = []
  let visited = []

  if(alphabet ==="A"){
    arr = itemA
    visited = visitedA
  }else{
    arr = itemB
    visited = visitedB
  }
  
  for(let i = start; i < arr.length; i++){
    let tmpSum = s + arr[i]
    if(!(visited[i])){
      visited[i] = true
      if(tmpSum <= C){
      if(alphabet ==="A"){
        ans+=1
        sumA.push(tmpSum)
        sumMaker(alphabet,tmpSum,i)
        visited[i] = false
      }else{
        ans+=1
        sumB.push(tmpSum)
        sumMaker(alphabet,tmpSum,i)
        visited[i] = false
      }
    }else{
      sumMaker(alphabet,tmpSum,i)
      visited[i] = false
      
    }

      
      
  }
    
       
  }

}


sumMaker("A",0,0)
sumMaker("B",0,0)
sumB.sort((a,b)=>a-b)

const binary = (n)=>{
  let start = 0
  let end = sumB.length
  
  while(start < end){
    const mid = Math.floor((start+end)/2)
    if(n + sumB[mid] <= C){
      
      start = mid + 1
    }else{
      end = mid
    }
  }

 
  ans += end
  
  
}

for(const num of sumA){
  binary(num)
}
console.log(ans)
process.exit()
})


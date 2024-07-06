const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout
})
let N = 0
let arr = []
let count = 0
rl.on("line",(line)=>{
    if(count === 0){
        N = Number(line.trim())
    }else{
        arr = line.trim().split(" ").map((el)=>Number(el))
        rl.close()
    }
    count++
})

rl.on("close",()=>{
    let a = arr.map((el,i)=>{
    el = [el,i]
    return el
})

let sortedArr = a.sort((a,b)=>a[0]-b[0])

let now = sortedArr[0][0]
let same = 0
let ans = []

for(let i = 0; i < N; i++){
   if(sortedArr[i][0] > now){
    same+=1
    now = sortedArr[i][0]
    ans.push([same,sortedArr[i][1]])
   }else{
    ans.push([same,sortedArr[i][1]])
   }
}
let answer =ans.sort((a,b)=>a[1]-b[1]).map((el)=>{
    let copy = el[0]
    return copy
})
console.log(...answer)

process.exit()    
})
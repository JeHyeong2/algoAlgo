const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout
})

let N = 0
let M = 0
let arrA = []
let arrB = []
let inputCount = 0

rl.on("line",(line)=>{
    let inp = line.trim().split(" ").map((el)=>Number(el))
    if(inputCount === 0){
        N = inp[0]
        M = inp[1]
    }else if(inputCount === 1){
        arrA = inp
    }else{
        arrB = inp
        rl.close()
    }
    
    inputCount +=1
})

rl.on("close",()=>{
    
const bSet = new Set(arrB)
let ans = []
let count = 0
for(let i = 0; i < arrA.length; i++){
    let numSet = bSet.size
    bSet.add(arrA[i])
    bSet.size === numSet ? "" : ans.push(arrA[i])
}
    
if(ans.length){

    ans.sort((a,b)=>a-b)
    console.log(ans.length)
    console.log(...ans)
}else{
    console.log(0)
}
    
process.exit()
    
})
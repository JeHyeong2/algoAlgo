const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout
})
let N = 0
const work = []
let inputCount = 0
rl.on("line",(line)=>{
    
    let inp = line.trim().split(" ").map((el)=>Number(el))
    
    if(inputCount == 0){
        N = inp[0]
    }else{
        work.push(inp)
    }
    if(inputCount == N){
        rl.close()
    }
    inputCount += 1
})

rl.on("close",()=>{
    let curWork = new Array(N+1).fill(0)

curWork[1] = work[0][0]

for(let i = 1; i < N; i++){
    
    let max_ = 0

    for(let j = 2; j < work[i].length; j++){

        curWork[work[i][j]] > max_ ? max_ = curWork[work[i][j]] : ""

    }

    curWork[i+1] = work[i][0] + max_

}

console.log(Math.max(...curWork))
})

const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout
})
let N = 0
let M = 0
rl.on("line",(line)=>{
    let inp = line.trim().split(" ").map((el)=>Number(el))
    N = inp[0]
    M = inp[1]
    rl.close()
})

rl.on("close",()=>{
    console.log(N.toString(M).toUpperCase())
    process.exit()
})
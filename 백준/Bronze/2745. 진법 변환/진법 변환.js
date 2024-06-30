const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout
})
let N = ""
let B = 0
rl.on("line",(line)=>{
    const inp = line.trim().split(" ")
    N = inp[0]
    B = inp[1]
})

rl.on("close",()=>{
    console.log(parseInt(N,B))
    process.exit()
})
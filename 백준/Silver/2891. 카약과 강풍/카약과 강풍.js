const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout
})

let inputCount = 0
let N = 0
let S = 0
let R = 0
let brokens = []
let spares = []

rl.on("line",(line)=>{
    let inp = line.trim().split(" ").map((el)=>Number(el))
    if(inputCount === 0){
        N = inp[0]
        S = inp[1]
        R = inp[2]
    }else if(inputCount === 1){
        brokens = inp
    }else{
        spares = inp
        rl.close()
    }
    inputCount++
})

rl.on("close",()=>{
 const boat = new Array(N+1).fill(1)
brokens.sort((a,b)=>a-b)
spares.sort((a,b)=>a-b)

for(const broke of brokens){
    boat[broke] = 0
}

for(let i = 0 ; i < R; i++){
    if(boat[spares[i]] === 0){
        boat[spares[i]] = 1
        spares[i] = 0
    }
}

for(let i = 0 ; i < R; i++){
    if(spares[i] > 0){
        if(boat[spares[i] - 1] === 0){
            boat[spares[i] -1] = 1
            spares[i] = 0
        }else if (boat[spares[i] + 1] === 0){
            boat[spares[i] +1] = 1
            spares[i] = 0
        }
    }
}

let count = 0
for(let i = 0; i < N+1; i++){
    boat[i] == 0 ? count +=1 : ""
}

console.log(count)

    
process.exit()
})
const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let inpC = 0
let N = 0
let lineN = 0
let words = ""
let arr = []
rl.on("line",(line)=>{
   if(inpC === 0){
       N = Number(line.trim())
   }else if(inpC===1){
       lineN = Number(line.trim())
   }else if(inpC ===2){
       words = line.trim()
   }else{
       arr.push(line.trim())
   }
    
    if(inpC ===line +2){
        rl.close()
    }
    
    inpC++
})

rl.on("close",()=>{
let result = []

for(let a of words){
    result.push(a.charCodeAt()-65)
}


let field = new Array(lineN+1).fill([]).map((el)=>{
    el = new Array(N).fill(-1)
    return el
})

for(let i = 0 ; i < N ; i++){
    field[0][i] = i
    field[lineN][i] = result[i]
}

let qLine = 0

for(let i = 0 ; i < lineN ; i++){
    if(arr[i][0] === "?"){
        qLine = i
        break
    }
    for(let j = 0 ; j < N-1; j++){
         if(arr[i][j] === "-"){
            field[i+1][j] = field[i][j+1]
            field[i+1][j+1] = field[i][j]
         }
    for(let j = 0 ; j < N ; j++){
        if(field[i+1][j] === -1){
            field[i+1][j] = field[i][j]
        }
    }
    }
}

for(let i = lineN-1 ; i>-1 ; i--){

    if(arr[i][0] === "?"){
        break
    }
    for(let j = 0 ; j < N-1; j++){
        if(arr[i][j] === "-"){
            field[i][j] = field[i+1][j+1]
            field[i][j+1] = field[i+1][j]
         }
    }
    for(let j = 0 ; j < N ; j++){
        if(field[i][j] === -1){
            field[i][j] = field[i+1][j]
        }
    }
}

let top = field[qLine]
let down = field[qLine+1]
let ans = ""

for(let i =0 ; i < N-1 ; i++){
    if(top[i]===down[i+1] && top[i+1]===down[i]){
        ans+="-"
    }else{
        ans+='*'
    }
}

let fc = new Array(N).fill(-1)
for(let i=0 ; i < ans.length ; i++){
    if(ans[i]==="-"){
        fc[i] = top[i+1]
        fc[i+1] = top[i]
    }
}
for(let i = 0; i < N ; i++){
    if(fc[i]===-1){
        fc[i] = top[i]
    }
}
if(fc.join("") === down.join("")){
    console.log(ans)
}else{
    console.log("x".repeat(N-1))
}
})
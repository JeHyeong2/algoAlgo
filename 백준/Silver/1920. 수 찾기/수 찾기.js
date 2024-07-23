const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})
let N = 0
let Narr = []
let M = 0
let Marr =[]
let inpC = 0 

rl.on("line",(line)=>{
    if(inpC ===0){
        N = Number(line.trim())
    }else if(inpC===1){
        Narr = line.trim().split(" ").map((el)=>Number(el))
    }else if(inpC===2){
        M = Number(line.trim())
    }else{
        Marr = line.trim().split(" ").map((el)=>Number(el))
    }
    
    if(inpC===3){
        rl.close()
    }
    
    inpC++    
})

rl.on("close",()=>{
    let result = ""

let a = new Set(Narr)

for(let i = 0 ; i < M; i++){
    a.has(Marr[i]) ? result+="1\n" : result +="0\n"
}
console.log(result)
})

const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})

let inpC = 0
let N = 0
let obj = {}
rl.on("line",(line)=>{
    if(inpC === 0){
        N = Number(line.trim())
    }else{
        let inp = line.trim().split(".")
        if (inp[1] in obj){
            obj[inp[1]] +=1
        }else{
            obj[inp[1]] = 1
        }
    }
    if(inpC===N){
        rl.close()
    }
    inpC++
})

rl.on("close",()=>{



let ac = Object.entries(obj)

ac.sort((a,b)=> a > b ? 1 : -1)

let result = ""
for(const as of ac){
    result += `${as.join(" ")}\n`
}
console.log(result)
})
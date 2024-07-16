const readline = require("readline")

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})
let inpCount = 0
let N = 0
let box = []
rl.on("line",(line)=>{

    if(inpCount === 0){
        N = Number(line.trim())
    }else{
        box = line.trim().split(" ").map((el)=>Number(el))
        rl.close()
    }

    inpCount++

})

rl.on("close",()=>{
    let _max = 1001
    let ans = 0
    const checkbox = new Array(N).fill(1)
    
    for(let i = 1 ; i < N ; i++){
        for(let j = 0 ; j < i; j++){
            if(box[i] > box[j]){
                checkbox[i] = Math.max(checkbox[i], checkbox[j]+1)
               
            }
        }
    }
console.log(Math.max(...checkbox))

    process.exit()
})




const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let inpC = 0
let N = 0
let M = 0
let max_weight = []
let box_weight = []
rl.on("line",(line)=>{
   if(inpC === 0){
       
       N = Number(line.trim())
       
   }else if(inpC ===1){
       
       let inp = line.trim().split(" ").map((el)=>Number(el))
       max_weight = inp  
       
   }else if(inpC===2){
       M = Number(line.trim())
       
   }else{
       
       let inp = line.trim().split(" ").map((el)=>Number(el))
       box_weight = inp
       rl.close()
   }
   inpC++
})

rl.on("close",()=>{

max_weight.sort((a,b)=>b-a)
box_weight.sort((a,b)=>b-a)

let count = 0 

if(box_weight[0]>max_weight[0]){
    console.log(-1)
}else{
    while(box_weight.length > 0){
        for(let crain of max_weight){
            for(let j =0 ; j < box_weight.length ; j++){
                if(box_weight[j] <= crain){
                    box_weight.splice(j,1)
                    break
                }
            }
            
        }
       


        count++        
        }
        console.log(count)
}


process.exit()
})
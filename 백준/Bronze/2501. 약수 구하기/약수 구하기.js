const readline = require("readline")

const rl = readline.createInterface({
    input : process.stdin,
    output : process.stdout
})
let a = 0
let b = 0
rl.on("line",(line)=>{
    inp = line.split(" ").map((el)=> Number(el))
    a = inp[0] 
    b = inp[1]
    rl.close()
})

rl.on("close",()=>{

  let count = 0
  for(let i = 1 ; i < a+1 ; i++){
    if(a % i === 0){
      count +=1
      if(count === b){
        console.log(i)
        process.exit()
          }
        }
      }
      console.log(0)
      process.exit()

    
})
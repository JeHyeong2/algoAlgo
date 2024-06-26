const readline = require("readline")
const rl = readline.createInterface({
  input : process.stdin,
  outpit : process.stdout
})
let N = 0
let count = 0
const tc = []
rl.on("line",(line)=>{
  if(count === 0){
    N = Number(line.trim())
  }else{
    tc.push(line.trim().split(" "))
  }
  count === N ? rl.close() : ""
  count+=1
})

rl.on("close",()=>{
  for(let i = 0; i < N; i++){
    let ans = ""
    for(let j = 0; j < tc[i][1].length; j++){
      ans += tc[i][1][j].repeat(tc[i][0])
    }
    console.log(ans)
  }
  process.exit()
})


const readline = require("readline")
const rl = readline.createInterface({
    input : process.stdin,
    output: process.stdout
})
let inputCount = 0
let N = 0
let M = 0
let K = 0
const mapArr = []
rl.on("line",(line)=>{
    if(inputCount ===0){
        let inp = line.trim().split(" ").map((el)=>Number(el))
        N = inp[0]
        M = inp[1]
        K = inp[2]
    }else{
        let inp = line.trim().split("").map((el)=>Number(el))
        mapArr.push(inp)
    }
    inputCount === N ? rl.close() : ""
    inputCount +=1
})

rl.on("close",()=>{
    class Node {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.size = 0;
    }
    enqueue(val) {
        let newNode = new Node(val);
        if (!this.first) {
            this.first = newNode;
            this.last = newNode;
        } else {
            this.last.next = newNode;
            this.last = newNode;
        }
        return ++this.size;
    }
    dequeue() {
        if (!this.first) return null;
        let temp = this.first;
        if (this.first === this.last) {
            this.last = null;
        }
        this.first = this.first.next;
        this.size--;
        return temp.value;
    }
}
const visited = new Array(N).fill([]).map((el)=>{
    el = new Array(M).fill([]).map((el)=>{
        el = new Array(K+1).fill(1000001)
        return el
    })
    return el
})


const di = [0,1,0,-1]
const dj = [1,0,-1,0]


const bfs = ()=>{
    
    let q = new Queue()
    q.enqueue([[0,0],0,1])
    while(q.size){
        
        let [now , broken, _sum] = q.dequeue()

        for (let k = 0; k < 4; k++){

            let ni = now[0] + di[k]
            let nj = now[1] + dj[k]
    
            if(0 <= ni && ni < N && 0 <= nj && nj < M){
    
                if(mapArr[ni][nj] === 1){
                    
                    if( broken < K && visited[ni][nj][broken+1] === 1000001){
                        visited[ni][nj][broken+1] = _sum + 1
                        q.enqueue([[ni,nj], broken+1, _sum + 1])
                    }
    
                }else{
                    if(visited[ni][nj][broken] === 1000001 ){
                        visited[ni][nj][broken] = _sum + 1
                        q.enqueue([[ni,nj], broken, _sum +1])
                    }
                }
    
            }
        }



    }
    

}

visited[0][0][0] = 1
bfs()


let ans = Math.min(...visited[N-1][M-1])
if(ans===1000001){
    console.log(-1)
}else{
    console.log(ans)
}



process.exit()
})
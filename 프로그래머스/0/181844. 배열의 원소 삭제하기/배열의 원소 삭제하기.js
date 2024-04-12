function solution(arr, delete_list) {
    let ans = []
    for(let i = 0 ; i<arr.length ; i++){
        let pass = true
        if(delete_list.includes(arr[i])){
           pass =false
           }
        pass ? ans.push(arr[i]) : ""
        }
    return ans;
    }
    

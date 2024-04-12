function solution(friends, gifts) {
    var answer = 0;
    const human = {}
    for(let i = 0 ; i < friends.length ; i++){
        human[friends[i]] = {total_give:0,total_get:0}
        for (let j =0; j < friends.length; j++){
            if(i !== j){
                human[friends[i]][friends[j]] = {give:0,get:0}
            }
        }
    }
    
    for (let i = 0 ; i < gifts.length ; i++){
        let info = gifts[i].split(" ")
            human[info[0]].total_give +=1
            human[info[1]].total_get +=1
            human[info[0]][info[1]].give +=1
            human[info[1]][info[0]].get +=1
    }
    
    for (let i = 0 ; i < friends.length ; i++){
        let count = 0 
        for (let j = 0; j < friends.length; j++){
            if(i!=j){
                if(human[friends[i]][friends[j]].give - human[friends[i]][friends[j]].get > 0){
                   count+=1
                }else if (human[friends[i]][friends[j]].give - human[friends[i]][friends[j]].get == 0){
                    let rank_me = human[friends[i]].total_give - human[friends[i]].total_get
                    let rank_compare = human[friends[j]].total_give - human[friends[j]].total_get
                    rank_me > rank_compare ? count+=1 : ""
                }
            }
        }
        answer = Math.max(count,answer)
    }
    
    
    
    return answer;
}
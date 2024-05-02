function solution(bandage, health, attacks) {
    var answer = 0;
    let maxNum = attacks[attacks.length-1][0] 
    let healCount = 0 
    const maxHp = health
    let hp = health
    
    for (let i = 1 ; i < maxNum+1 ; i++){
        
        
        
        if (i == attacks[0][0] ){
            hp = hp - attacks[0][1]
            attacks.shift()
            healCount = 0
            if(hp <= 0){
            return -1
        }
            continue
        }
        
        healCount += 1
        hp += bandage[1]

        if(healCount == bandage[0]){
            hp += bandage[2]
            healCount = 0 
        }
        if(hp > maxHp){
            hp = maxHp
        }
    
    } 
    
    return hp
}
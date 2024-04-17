function solution(record) {
    let user = {};
    let result = [];
    
    for (let r of record) {
        //배열 구조분해
        const [command,uid,name] = r.split(" ");
        
        if (command === "Enter"){
            user[uid] = name; //객체[키] = 값
            result.push(`${uid}님이 들어왔습니다.`);
        }
        else if (command === "Leave"){
            result.push(`${uid}님이 나갔습니다.`);
        }
        else if (command === "Change"){
            user[uid] = name; //바꿈
        }  
    }
    
    //result 배열: replace(바꿀대상, newName)
    //id를 최신 name으로 update -> user객체에 저장되어 있음
    //값을 재할당할때는 for문을 써야한다!!! for of문 쓰면 임시변수에 값이 할당되는 것이므로 result배열에는 반영안됨
    for(let i=0;i<result.length;i++){ //id로 저장해놓음
        const id = result[i].split("님이")[0]; //id만 추출
        result[i] = result[i].replace(id, user[id]);
    }
    return result;
    
    
}
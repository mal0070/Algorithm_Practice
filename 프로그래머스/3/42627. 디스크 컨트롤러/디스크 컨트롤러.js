function solution(jobs) {
    let answer = 0;
    let jobsCnt = jobs.length; //이거 따로 저장안하면 null나옴..왜지
    let waitingList = []; //대기 리스트 -> 요청시점 지난 작업들. 처리시간으로 정렬하고 순서대로 처리
    
   let jobList = jobs.sort((a,b) => {
       if (a[0] === b[0]) {return a[1]-b[1]} //요청시간 같으면 처리시간 짧은 순서로
       else {return a[0]-b[0]}
   }); //요청시간 순서대로 정렬
    
    let currentTime = jobList[0][0]; //현재 시간
    
    //각 시점에서 처리시간 짧은 것 선택
    while (jobList.length > 0){
        let job = jobList[0];  // 요청시간 가장 빠른 것 선택
        if(currentTime > job[0]){ //선택한 것의 요청시간이 지났다면, waitingList에 적재
            waitingList.push(job);
            jobList.shift();
        } else { //안지났다면, 처리
            if (waitingList.length > 0){ //대기중인게 있음
                waitingList.sort((a,b) => a[1]-b[1]);
                let waitJob = waitingList.shift();
                currentTime += waitJob[1];
                answer += currentTime - waitJob[0];//요청시점의 시간 뺌
            } else{ //대기하는게 없으면
                currentTime = job[0] + job[1]; //처리
                answer += job[1];
                jobList.shift();
            }
        }
        
        //남아있는 작업이 없고, 모두 대기중일때
        if (jobList.length === 0 && waitingList.length >0){
            waitingList.sort((a,b) => a[1]-b[1]);
            while (waitingList.length > 0){
                let waitJob = waitingList.shift();
                currentTime += waitJob[1];
                answer += currentTime - waitJob[0]; 
            }
        }
        
    }
    
    
    return Math.floor(answer/jobsCnt); //버림
}
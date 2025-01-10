function solution(id_list, report, k) {
    const idCount = id_list.length;
    const result = Array(idCount).fill(0); //각 유저별 신고 당한 횟수
    const uniqueReport = [...new Set(report)]; //중복이 제거된 신고 리스트
    const record = Array.from({length: idCount}, ()=>[]); //신고기록
    let answer = Array(idCount).fill(0); //각 유저별로 처리 결과 메일을 받은 횟수 
    
    uniqueReport.forEach((item)=>{
        const [user, reportedUser] = item.split(' ');
        
            //신고 당한 횟수 업데이트
            const reportedUserIndex = id_list.indexOf(reportedUser);
            result[reportedUserIndex]++;
            //신고 기록 업데이트
            const userIndex = id_list.indexOf(user);
            record[userIndex].push(reportedUser);
    });
    
    result.forEach((time, index)=>{
        if(time>=k){
            record.forEach((row, i)=>{
               if(row.includes(id_list[index]))
                   answer[i]++;
            })
        }
    });
    
    return answer; 
}
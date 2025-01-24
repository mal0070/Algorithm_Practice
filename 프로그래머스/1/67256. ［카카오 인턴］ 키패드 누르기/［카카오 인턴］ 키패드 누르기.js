function solution(numbers, hand) {
    //거리 계산 => 좌표를 만든다
    const keypad = {
        1:[0,0], 2:[0,1], 3:[0,2],
        4:[1,0], 5:[1,1], 6:[1,2],
        7: [2,0], 8:[2,1], 9:[2,2],
        '*':[3,0], 0:[3,1], '#':[3,2]
    };
    
    let leftPos = '*';
    let rightPos = '#';
    const answer = [];
    
    //거리 계산 함수
    const getDistance = (pos1,pos2) => {
        const [x1, y1] = keypad[pos1];
        const [x2, y2] = keypad[pos2];
        return Math.abs(x1-x2) + Math.abs(y1-y2);
    }

    numbers.forEach((number)=>{
        if([1,4,7].includes(number)){
            answer.push('L');
            leftPos = number;
        } else if ([3,6,9].includes(number)){
            answer.push('R');
            rightPos = number;
        } else {
            //거리비교
            const leftDis = getDistance(leftPos, number);
            const rightDis = getDistance(rightPos, number);
            
            if(leftDis < rightDis){
                answer.push('L');
                leftPos = number;
            } else if (leftDis > rightDis) {
                answer.push('R');
                rightPos = number;
            } else {
                if(hand === 'right') {
                    answer.push('R');
                    rightPos = number;
                } else {
                    answer.push('L');
                    leftPos = number;
                }
            }
            
        }
    });
  
    return answer.join('');
}
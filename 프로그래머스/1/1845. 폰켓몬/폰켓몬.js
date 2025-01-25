function solution(nums) {
    const pick = nums.length /2;
    const newNums = [...new Set(nums)]; //중복이 제거된 숫자 리스트

    if (pick>=newNums.length){
        return newNums.length;
    } else { //pick < newNums.length
        return pick;
    }
}
//직사각형이라는 특징 생각. 잘못된 입력 주어지지 않음!
function solution(dots) {
    dots.sort((a,b)=>a[0]-b[0])//x값 작은 순서대로 정렬. 직사각형이니까
    const side1 = Math.abs(dots[0][1]-dots[1][1]); //y값 계산 -> 세로
    const side2 = Math.abs(dots[1][0]-dots[2][0]) //가로
    return side1 * side2
}

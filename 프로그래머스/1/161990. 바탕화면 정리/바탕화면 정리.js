function solution(wallpaper) { //문자열 인덱스 접근 가능
    let indexSet = [];
    
    for(let i=0;i<wallpaper.length;i++){
        for(let j=0;j<wallpaper[i].length;j++){
            if(wallpaper[i][j] === "#")
                indexSet.push([i,j]); //굳이 객체로 안해도 됨. 인덱스만 저장하면 됨
        }
    }
    let minX = 50;
    let minY = 50;
    let maxX = 0;
    let maxY = 0;
    for (index of indexSet){
        minX = Math.min(minX,index[0]);
        minY = Math.min(minY, index[1]);
        maxX = Math.max(maxX, index[0]); //여기서 구한건 점이므로 +1해서 #포함시켜주어야함
        maxY = Math.max(maxY, index[1]);
    }
    return ([minX, minY, maxX+1, maxY+1]);
}


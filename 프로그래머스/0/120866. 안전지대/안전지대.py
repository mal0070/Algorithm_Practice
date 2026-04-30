def solution(board):
    directions = [-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[0,0] #상~시계방향, 본인
    answer = 0
    
    n = len(board) #y
    m = len(board[0]) #x
    
    d_board = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                for [dy, dx] in directions:
                    iy = i + dy
                    ix = j + dx
                    
                    if ix >= 0 and ix<m and iy>=0 and iy<n:
                         d_board[iy][ix] = 1 #marked
    
    for i in range(n):
        for j in range(m):
            if d_board[i][j] == 0:
                answer +=1
    
    return answer
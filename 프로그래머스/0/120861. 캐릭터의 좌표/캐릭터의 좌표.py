def solution(keyinput, board):
    pos = [0,0]
    x = board[0]//2 #4
    y = board[1]//2 #2
    #keys = [[0,1],[0,-1],[-1,0],[1,0]] #up, down, left, right
    
    for key in keyinput:
        if key == "up":
            if pos[1] < y :
                pos[1] += 1
            else:
                continue
        if key == "down":
            if pos[1] > -y :
                pos[1] += -1
            else:
                continue
        if key == "left":
            if pos[0] > -x: #옆으로 갈 수 있는 칸이 남아 있을 때
                pos[0] += -1
            else:
                continue
        if key == "right": 
            if pos[0] < x: 
                pos[0] += 1
            else:
                continue
        
    return pos



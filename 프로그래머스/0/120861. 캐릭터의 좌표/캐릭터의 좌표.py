def solution(keyinput, board):
    len_x = board[0]//2
    len_y = board[1]//2
    
    direction = {"up":(0,1), "down":(0,-1),
                "left":(-1,0), "right":(1,0)}
    x,y = 0,0
    
    for i in keyinput:
        direction_x, direction_y = direction[i]
        if abs(x+direction_x) > len_x or abs(y+direction_y) > len_y:
            continue
        
        else:
            x,y = (x+direction_x),(y+direction_y)
        
    return [x,y]
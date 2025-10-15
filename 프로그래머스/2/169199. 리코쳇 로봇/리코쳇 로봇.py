from collections import deque

def solution(board):
    x_len = len(board)
    y_len = len(board[0])
    dequee = deque()
    
    r_x = 0
    r_y = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    visited=set()
    
    for i in range(x_len):
        for j in range(y_len):
            if(board[i][j] == "R"):
                r_x = i
                r_y = j
                
    dequee.append((r_x,r_y,0))
    visited.add((r_x,r_y))
    
    while(dequee):
        x,y,cost = dequee.popleft()
        
        if(board[x][y] == "G"):
            return cost
            
        for i in range(4):
            nx = x 
            ny = y
            
            while(True):
                tx = nx + dx[i]
                ty = ny + dy[i]
                
                if 0 <= tx < x_len and 0 <= ty < y_len and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
                    
            if((nx,ny) not in visited):
                visited.add((nx,ny))
                dequee.append((nx,ny,cost+1))
            
    return -1
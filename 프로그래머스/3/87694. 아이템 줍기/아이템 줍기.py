from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board=[[-1 for _ in range(101)] for _ in range(101)]
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    def dfs(x,y):
        nonlocal visited
        
        dq=deque()
        dq.append((x,y,0))
        
        while(dq):
            cx,cy,count=dq.popleft()
            
            if(cx==itemX*2 and cy==itemY*2):
                return count
            
            for i in range(4):
                nx=cx+dx[i]
                ny=cy+dy[i]
                
                if(0<=nx<101 and 0<=ny<101 and board[nx][ny]==2 and not visited[nx][ny]):
                    visited[nx][ny]=True
                    dq.append((nx,ny,count+1))
            
    #테두리 칠하기
    for i in range(len(rectangle)):
        s_x,s_y,e_x,e_y=rectangle[i][0]*2,rectangle[i][1]*2,rectangle[i][2]*2,rectangle[i][3]*2
        for j in range(s_x,e_x+1):
            for k in range(s_y,e_y+1):
                if(j==s_x or j==e_x or k==s_y or k==e_y):
                    if(board[j][k]==-1):
                        board[j][k]=2 #선이 2
                else:
                    board[j][k]=1
    
    count=0
    visited=[[False for _ in range(101)] for _ in range(101)]
    visited[characterX*2][characterY*2]=True
    
    return dfs(characterX*2,characterY*2)//2
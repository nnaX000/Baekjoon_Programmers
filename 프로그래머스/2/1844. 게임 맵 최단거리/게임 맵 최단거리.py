from collections import deque
def solution(maps):
    
    visited=[[False for i in range(len(maps[0]))] for j in range(len(maps))]
    visited[0][0]=True
    min_value=[float('inf')]
    x_num=len(maps)-1
    y_num=len(maps[0])-1
    dequee=deque([[0,0,1]])
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    while(dequee):
        x,y,score=dequee.popleft()
        
        if(x==x_num and y==y_num):
            min_value[0]=score
            break
            
        for i in range(4):
            new_x=x+dx[i]
            new_y=y+dy[i]
            
            if(0<=new_x<=x_num and 0<=new_y<=y_num and maps[new_x][new_y]==1 and not visited[new_x][new_y]):
                score+=1
                visited[new_x][new_y]=True
                dequee.append([new_x,new_y,score])
                score-=1
                
    
    if(min_value[0]==float('inf')):
        min_value[0]=-1
    
    return min_value[0]
    
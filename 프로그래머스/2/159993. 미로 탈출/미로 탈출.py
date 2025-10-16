#S : 시작 지점
#E : 출구
#L : 레버
#O : 통로
#X : 벽
#시작 -> 레버 -> 출구
#레버 안돌려도 출구 칸 지나갈 수 O
from collections import deque
def solution(maps):
    min_value = float('inf')
    dequee=deque()
    
    x_len = len(maps)
    y_len = len(maps[0])
    
    start_x = 0
    start_y = 0
    lever_x = 0
    lever_y = 0
    exit_x = 0
    exit_y = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = set()
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if(maps[i][j]=="S"):
                start_x=i
                start_y=j
                
            if(maps[i][j]=="L"):
                lever_x=i
                lever_y=j
                
            if(maps[i][j]=="E"):
                exit_x=i
                exit_y=j
                
    dequee.append((start_x,start_y,False,0)) # 현재위치 x, 현재위치 y, 레버 돌린 여부, cost
    visited.add((start_x,start_y,False))
    
    while(dequee):
        x,y,lever,cost = dequee.popleft()
        
        if(x==exit_x and y==exit_y and lever):
            min_value = min(min_value,cost)
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if(0<=nx<x_len and 0<=ny<y_len and (nx,ny,lever) not in visited and maps[nx][ny]!="X"):
                if(nx == lever_x and ny == lever_y and not lever):
                    dequee.append((nx,ny,True,cost+1))
                    visited.add((nx,ny,True))
                else:
                    dequee.append((nx,ny,lever,cost+1))
                    visited.add((nx,ny,lever))
                    
        
    return min_value if min_value != float('inf') else -1
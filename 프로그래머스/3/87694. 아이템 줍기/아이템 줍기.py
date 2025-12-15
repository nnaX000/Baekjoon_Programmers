from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    boards=[[0 for i in range(101)] for j in range(101)]
    dequee=deque()
    visited=[[False for i in range(101)] for j in range(101)]
    dequee.append((characterX*2,characterY*2,0,visited)) # 위치, cost, visited
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    # 일단 직사각형 다 칠하기
    for a,b,c,d in rectangle:
        for i in range(a*2,(c*2)+1):
            for j in range(b*2,(d*2)+1):
                boards[i][j]=1 # 접근 가능
    
    # 테두리 빼고 다 접근불가 처리
    for a,b,c,d in rectangle:
        for i in range((a*2)+1,c*2):
            for j in range((b*2)+1,d*2):
                boards[i][j]=0
                
    while(dequee):
        x,y,cost,visited=dequee.popleft()
        
        if(x==itemX*2 and y==itemY*2):
            answer=cost
            break
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            n_visited=[j[:] for j in visited]
            
            if(0<=nx<101 and 0<=ny<101 and boards[nx][ny]==1 and not n_visited[nx][ny]):
                n_visited[nx][ny]=True
                dequee.append((nx,ny,cost+1,n_visited))
    
    return answer//2
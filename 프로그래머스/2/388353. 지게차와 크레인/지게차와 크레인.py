from collections import defaultdict,deque
import sys

#지게차는 접가한 컨테이너만 꺼낼 수 있음 접근이 가능한 컨테이너란 4면 중 적어도 1면이 창고 외부와 연결됨.
#크레인은 접근 불가한 것도 꺼낼 수 있음.

sys.setrecursionlimit(10**6)

def solution(storage, requests):
    answer = 0
    alpha=defaultdict(deque)
    row=len(storage)
    column=len(storage[0])
    s=[[0 for _ in range(column+2)] for _ in range(row+2)]
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    #외부와 연결되어 있는지 갱신
    def dfs(x,y):
        nonlocal visited
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if(0<=nx<row+2 and 0<=ny<column+2 and (s[nx][ny]==1 or s[nx][ny]==0) and not visited[nx][ny]):
                s[nx][ny]=0
                visited[nx][ny]=True
                dfs(nx,ny)
    
    for i in range(1,row+1):
        for j in range(1,column+1):
            s[i][j]=storage[i-1][j-1]
            alpha[storage[i-1][j-1]].append([i,j])
    
    for i in range(len(requests)):
        command=requests[i]
        stand=command[0]
        
        #환기
        visited=[[False for _ in range(column+2)] for _ in range(row+2)]
        dfs(0,0)
        
        num=len(alpha[stand])
        count=0
        
        if(len(command)==1):
            while(count<num and alpha[stand]):
                x,y=alpha[stand].popleft()
                check=False
                
                for j in range(4):
                    nx=x+dx[j]
                    ny=y+dy[j]
                    
                    if(0<=nx<row+2 and 0<=ny<column+2 and s[nx][ny]==0):
                        check=True
                        break
                        
                if(check):
                    s[x][y]=1
                else:
                    alpha[stand].append([x,y])
                    
                count+=1
        else:
            while(alpha[stand]):
                x,y=alpha[stand].popleft()
                s[x][y]=1           
    
    for i in range(1,row+1):
        for j in range(1,column+1):
            if(s[i][j]!=1 and s[i][j]!=0):
                answer+=1
                
    return answer
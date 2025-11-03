import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    row = len(maps)
    column = len(maps[0])
    
    visited = [[False for i in range(column)] for j in range(row)]
    
    def dfs(x,y):
        nonlocal result
        
        for i in range(4):
            if(0<=x+dx[i]<row and 0<=y+dy[i]<column and maps[x+dx[i]][y+dy[i]] != "X" and not visited[x+dx[i]][y+dy[i]]):
                visited[x+dx[i]][y+dy[i]] = True
                dfs(x+dx[i],y+dy[i])
                result+=int(maps[x+dx[i]][y+dy[i]])
    
    for i in range(row):
        for j in range(column):
            if(not visited[i][j] and maps[i][j] != "X"):
                result = int(maps[i][j])
                visited[i][j] = True
                dfs(i,j)
                answer.append(result)
    
    answer.sort()
    
    return answer if len(answer)>0 else [-1]
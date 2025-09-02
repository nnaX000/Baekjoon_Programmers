import sys

sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline().rstrip())

board=[list(sys.stdin.readline().rstrip()) for i in range(N)]

visited=[[0 for i in range(N)] for j in range(N)]

dx=[0,0,1,1,-1,-1]
dy=[-1,1,-1,0,0,1]

answer=0

def dfs(x,y):
    global answer
    global visited
    answer=max(answer,1)
    
    for i in range(6):
        if(0<=x+dx[i]<N and 0<=y+dy[i]<N and board[x+dx[i]][y+dy[i]]=="X"):
            nx=x+dx[i]
            ny=y+dy[i]
            if(visited[nx][ny]==0):
                visited[nx][ny]=-visited[x][y]
                dfs(nx,ny)
                answer=max(answer,2)
            else:
                if visited[nx][ny]==visited[x][y]:
                    answer=max(answer,3)
                    return
    
for i in range(N):
    for j in range(N):
        if(board[i][j]=="X" and visited[i][j]==0):
            visited[i][j]=1
            dfs(i,j)

print(answer)
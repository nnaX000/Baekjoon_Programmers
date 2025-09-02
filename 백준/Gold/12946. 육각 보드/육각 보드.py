import sys

sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline().rstrip())

board=[list(sys.stdin.readline().rstrip()) for i in range(N)]

visited=[[-1 for i in range(N)] for j in range(N)]

dx=[0,0,1,1,-1,-1]
dy=[-1,1,-1,0,0,1]

answer=0

def dfs(x,y,color):
    global answer
    global visited
    answer=max(answer,1) #어쨌든 X가 하나있으면 무조건 1개 색은 칠해야 함.

    for i in range(6):
        if(0<=x+dx[i]<N and 0<=y+dy[i]<N and board[x+dx[i]][y+dy[i]]=="X"):
            nx=x+dx[i]
            ny=y+dy[i]
            if(visited[nx][ny]==-1):
                visited[nx][ny]=color
                dfs(nx,ny,1-color)
                answer=max(answer,2) # 인접한게 있으면 무조건 2개 색 필요함.
            else:
                if visited[nx][ny]==1-color:
                    answer=max(answer,3) #이미 칠해져있는데 그게 내 색이랑 똑같으면 3개 색 필요함.
                    return
    
for i in range(N):
    for j in range(N):
        if(board[i][j]=="X" and visited[i][j]==-1):
            visited[i][j]=0
            dfs(i,j,1)

print(answer)
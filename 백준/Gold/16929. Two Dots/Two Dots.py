import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
board=[sys.stdin.readline().rstrip() for i in range(N)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y,visited,color):
    if((x,y-1)==(origin_x,origin_y) and len(visited)>=4):
        print("Yes")
        sys.exit(0)

    for i in range(4):
        if(0<=x+dx[i]<N and 0<=y+dy[i]<M and (x+dx[i],y+dy[i]) not in visited and board[x+dx[i]][y+dy[i]]==color):
            nx=x+dx[i]
            ny=y+dy[i]
            visited.add((nx,ny))
            dfs(nx,ny,visited,color)
            visited.remove((nx,ny))
    
for i in range(N):
    for j in range(M):
        visited=set()
        visited.add((i,j))
        origin_x=i
        origin_y=j
        dfs(i,j,visited,board[i][j])

print("No")
import sys
from collections import deque

input=sys.stdin.readline

R,C=map(int,input().split()) #행 개수, 열 개수

maze=[list(input().rstrip()) for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

j_x=0
j_y=0

dq=deque()

for i in range(R):
    for j in range(C):
        if(maze[i][j]=="J"):
            j_x=i
            j_y=j
            maze[i][j]="."

        if(maze[i][j]=="F"):
            maze[i][j]=0
            dq.append((i,j,0))

while(dq):
    cx,cy,cost=dq.popleft()

    for i in range(4):
        nx=cx+dx[i]
        ny=cy+dy[i]

        if(0<=nx<R and 0<=ny<C and maze[nx][ny]=="."):
            dq.append((nx,ny,cost+1))
            maze[nx][ny]=cost+1

dq=deque()
dq.append((j_x,j_y,0))
visited=[[False for _ in range(C)] for _ in range(R)]

while(dq):
    x,y,cost=dq.popleft()

    if(x==0 or x==R-1):
        print(cost+1)
        sys.exit(0)

    if(y==0 or y==C-1):
        print(cost+1)
        sys.exit(0)
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<R and 0<=ny<C and maze[nx][ny]!="#" and not visited[nx][ny]):
            if(maze[nx][ny]=="."):
                visited[nx][ny]=True
                dq.append((nx,ny,cost+1))
            else:
                if(maze[nx][ny]>cost+1):
                    visited[nx][ny]=True
                    dq.append((nx,ny,cost+1))

print("IMPOSSIBLE")
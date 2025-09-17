import sys
from collections import deque

dequee=deque()
board=[list(sys.stdin.readline().rstrip()) for i in range(8)]

dx=[-1,1,0,0,-1,1,0,1,-1]
dy=[0,0,-1,1,-1,1,0,-1,1]

visited=set()
wall=set()

for i in range(8):
    for j in range(8):
        if(board[i][j]=="#"):
            wall.add((i,j))

dequee.append((7,0,wall,0)) # x좌표, y좌표, wall, 시간
visited.add((7,0,0)) # x좌표, y좌표, 시간

while(dequee):
    x,y,wall,time = dequee.popleft()
    new_wall=set()
    nt=time+1

    for wall_x,wall_y in wall:
        if(wall_x+1<8):
            new_wall.add((wall_x+1,wall_y))

    if(x==0 and y==7):
        print(1)
        sys.exit(0)

    for i in range(9):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<8 and 0<=ny<8 and (nx,ny) not in wall and (nx,ny) not in new_wall and (nx,ny,nt) not in visited):
            dequee.append((nx,ny,new_wall,nt))
            visited.add((nx,ny,nt))

print(0)
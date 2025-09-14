import sys
from collections import deque

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
graph=[list(map(int,sys.stdin.readline().rstrip())) for i in range(N)]
min_value=float('inf')
dx=[-1,1,0,0]
dy=[0,0,-1,1]

dequee=deque()
dequee.append([0,0,0])
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0]=1

while(dequee):
    tmp=dequee.popleft()
    nx=tmp[0]
    ny=tmp[1]
    count=tmp[2]

    if(nx==N-1 and ny==M-1):
        min_value=min(min_value,visited[nx][ny][count])
        break

    for j in range(4):
        nx_x=nx+dx[j]
        ny_y=ny+dy[j]

        if(0<=nx_x<N and 0<=ny_y<M and visited[nx_x][ny_y][count]==0):
            if(graph[nx_x][ny_y]==0):
                dequee.append([nx_x,ny_y,count])
                visited[nx_x][ny_y][count]=visited[nx][ny][count]+1
            elif(graph[nx_x][ny_y]==1 and count==0):
                dequee.append([nx_x,ny_y,count+1])
                visited[nx_x][ny_y][count+1]=visited[nx][ny][count]+1

if(min_value==float('inf')):
    print(-1)
else:
    print(min_value)
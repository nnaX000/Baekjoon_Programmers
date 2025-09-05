import sys
from collections import deque

N=int(sys.stdin.readline().rstrip())
dequee=deque()

r_1,c_1,r_2,c_2=map(int,sys.stdin.readline().rstrip().split(' '))

dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]

dequee.append([r_1,c_1])
visited=[[-1 for i in range(N)] for j in range(N)]
visited[r_1][c_1]=0

while(dequee):
    x,y=dequee.popleft()

    for i in range(6):
        n_x=x+dx[i]
        n_y=y+dy[i]

        if(0<=n_x<N and 0<=n_y<N and visited[n_x][n_y]==-1):
            visited[n_x][n_y]=visited[x][y]+1
            dequee.append([n_x,n_y])

    if(visited[r_2][c_2]!=-1):
        print(visited[r_2][c_2])
        break

if(visited[r_2][c_2]==-1):
    print(-1)
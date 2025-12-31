import sys
from collections import deque

#다익스트라..가 아니라 bfs?

input=sys.stdin.readline

n,m=map(int,input().split())

land=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=[]

target_x=0
target_y=0

dequee=deque()

for i in range(n):
    for j in range(m):
        if(land[i][j]==1):
            land[i][j]=-1
        elif(land[i][j]==2):
            target_x=i
            target_y=j
            land[i][j]=0
            dequee.append((i,j))

while(dequee):
    x,y=dequee.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<n and 0<=ny<m and land[nx][ny]==-1):
            land[nx][ny]=land[x][y]+1
            dequee.append((nx,ny))

for i in land:
    print(*i)
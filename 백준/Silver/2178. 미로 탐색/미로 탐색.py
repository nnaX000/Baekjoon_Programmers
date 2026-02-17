import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

maze=[list(map(int,input().rstrip())) for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

dq=deque()
dq.append((0,0,1)) #x,y,cost

# 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸

visited=[[False for _ in range(M)] for _ in range(N)]
visited[0][0]=True

while(dq):
    x,y,cost=dq.popleft()

    if(x==N-1 and y==M-1):
        print(cost)
        sys.exit(0)

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<M and maze[nx][ny]==1 and not visited[nx][ny]):
            visited[nx][ny]=True
            dq.append((nx,ny,cost+1))   
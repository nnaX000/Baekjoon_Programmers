import sys
from collections import deque

input=sys.stdin.readline

# 벽 한개까지 부수고 이동 가능
# 1은 이동할 수 없는 벽

dx=[-1,1,0,0]
dy=[0,0,-1,1]

N,M=map(int,input().split())
maps=[list(map(int,input().rstrip())) for _ in range(N)]
dequee=deque()
dequee.append((0,0,0))
visited=[[[float('inf'),float('inf')] for _ in range(M)] for _ in range(N)]

visited[0][0][0]=1
visited[0][0][1]=1

while(dequee):
    x,y,b=dequee.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<M):
            if(maps[nx][ny]==0 and visited[nx][ny][b]==float('inf')):
                dequee.append((nx,ny,b))
                visited[nx][ny][b]=visited[x][y][b]+1
            elif(maps[nx][ny]==1 and b==0 and visited[nx][ny][1]==float('inf')):
                dequee.append((nx,ny,1))
                visited[nx][ny][1]=visited[x][y][b]+1

print(min(visited[N-1][M-1]) if min(visited[N-1][M-1])!=float('inf') else -1)
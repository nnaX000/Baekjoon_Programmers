import sys
from collections import deque

input=sys.stdin.readline

N,M,K=map(int,input().split())

# .은 빈칸, #은 벽
gym=[list(input().rstrip()) for _ in range(N)]

x1,y1,x2,y2=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

dequee=deque()
dequee.append((x1-1,y1-1))
visited=[[float('inf') for _ in range(M)] for _ in range(N)]
visited[x1-1][y1-1]=0

while(dequee):
    x,y=dequee.popleft()

    if(x==x2-1 and y==y2-1):
        print(visited[x2-1][y2-1])
        sys.exit(0)

    for i in range(4):
        for j in range(1,K+1):
            nx=x+(dx[i]*j)
            ny=y+(dy[i]*j)

            if(0<=nx<N and 0<=ny<M and visited[nx][ny] >= visited[x][y] + 1 and gym[nx][ny]=="."):
                if(visited[nx][ny] > visited[x][y] + 1):
                    visited[nx][ny]=visited[x][y]+1
                    dequee.append((nx,ny))
            else:
                break

print(-1)
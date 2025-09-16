import sys
from collections import deque

N,M,K=map(int,sys.stdin.readline().rstrip().split(' '))
graph=[list(map(int,sys.stdin.readline().rstrip())) for i in range(N)]
dp = [[[-1]*(K+1) for _ in range(M)] for _ in range(N)]
dp[0][0][0]=1

dequee=deque()
dequee.append([0,0,0])

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while(dequee) :
    tmp=dequee.popleft()

    x=tmp[0]
    y=tmp[1]
    count=tmp[2]

    if(x==N-1 and y==M-1):
        print(dp[x][y][count])
        sys.exit(0)

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<M):
            if(graph[nx][ny]==0 and dp[nx][ny][count]==-1):
                dp[nx][ny][count]=dp[x][y][count]+1
                dequee.append([nx,ny,count])
            elif(graph[nx][ny]==1 and count<K):
                if(dp[nx][ny][count+1]==-1):
                    dp[nx][ny][count+1]=dp[x][y][count]+1
                    dequee.append([nx,ny,count+1])

print(-1)
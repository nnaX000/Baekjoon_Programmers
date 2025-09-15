import sys
from collections import deque

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

graph=[list(map(int,sys.stdin.readline().rstrip())) for i in range(N)]

answer=[[0 for i in range(M)]for j in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

group=[[-1 for i in range(M)]for j in range(N)]
group_size=[]
group_number=0

for i in range(N):
    for j in range(M):
        if(graph[i][j]==0 and group[i][j]==-1):
            dequee=deque()
            group[i][j]=group_number
            dequee.append([i,j])
            result=1
            while(dequee):
                tmp=dequee.popleft()
                x=tmp[0]
                y=tmp[1]
                for k in range(4):
                    nx=x+dx[k]
                    ny=y+dy[k]
                    if(0<=nx<N and 0<=ny<M and graph[nx][ny]==0 and group[nx][ny]==-1):
                        result+=1
                        group[nx][ny]=group_number
                        dequee.append([nx,ny])

            group_number+=1
            group_size.append(result)

for i in range(N):
    for j in range(M):
        if(graph[i][j]==1):
            answer[i][j]=1
            visit=set()
            for k in range(4):
                nx=i+dx[k]
                ny=j+dy[k] 
                if(0<=nx<N and 0<=ny<M and graph[nx][ny]==0 and group[nx][ny] not in visit):
                    answer[i][j]+=((group_size[group[nx][ny]]))
                    visit.add(group[nx][ny])
            answer[i][j]%=10

for i in range(N):
    for j in range(M):
        print(answer[i][j],end="")
    print()
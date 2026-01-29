import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

# 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 
# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

# 0 빈칸, 1은 벽, 2는 비활성 바이러스 위치

labs=[list(map(int,input().split())) for _ in range(N)]
vacant=[]
answer=float('inf')
vacant_num=0

for i in range(N):
    for j in range(N):
        if(labs[i][j]==2):
            vacant.append([i,j])
        if(labs[i][j]==0):
            vacant_num+=1

if(vacant_num==0):
    print(0)
    sys.exit(0)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

candi=[]

# 놓을 수 있는 바이러스 조합 구하기
def dfs(start,array):
    global candi

    if(len(array)==M):
        candi.append(array[:])
        return

    for i in range(start,len(vacant)):
        array.append(vacant[i])
        dfs(i+1,array)
        array.pop()

dfs(0,[])

#바이러스 퍼지는 속도 구하기
def bfs(dequee):
    global time
    global count
    global visited

    while(dequee):
        x,y=dequee.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<N and 0<=ny<N and visited[nx][ny]==float('inf') and labs[nx][ny]!=1):
                dequee.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1

                if(labs[nx][ny]==0):
                    time=max(time,visited[nx][ny])
                    count+=1

for i in range(len(candi)):
    dequee=deque(candi[i])
    visited=[[float('inf') for _ in range(N)] for _ in range(N)]

    time=0
    count=0

    for x,y in candi[i]:
        visited[x][y]=0

    bfs(dequee)

    if(count==vacant_num):
        answer=min(time,answer)

print(answer if answer!=float('inf') else -1)
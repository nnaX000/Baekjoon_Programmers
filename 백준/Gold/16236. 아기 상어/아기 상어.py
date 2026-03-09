import sys
import heapq
from collections import deque

input=sys.stdin.readline

N=int(input())

space=[list(map(int,input().split())) for _ in range(N)]

#0 빈칸
#1 2 3 4 5 6 물고기
# 9 아기상어

# 처음 아기상어 크기2
# 크기가 같은 물고기는 지나갈수밖에 없고 크기가 작은 물고기는 잡아먹을 수 있음
# 거리가 가까운 물고기가 많으면 가장 위에 있는, 가장 왼쪽에 있는 물고기

baby_x=0
baby_y=0

baby_s=2
count=2

time=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    for j in range(N):
        if(space[i][j]==9):
            baby_x,baby_y=i,j
            space[i][j]=0

def calcul():
    global space
    global hq

    dq=deque()
    dq.append((baby_x,baby_y,0))

    visited=[[False for _ in range(N)] for _ in range(N)]
    visited[baby_x][baby_y]=True

    while(dq):
        x,y,cost=dq.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<N and 0<=ny<N and space[nx][ny]<=baby_s and not visited[nx][ny]):
                visited[nx][ny]=True
                dq.append((nx,ny,cost+1))
                if(space[nx][ny]!=0):
                    heapq.heappush(hq,(cost+1,nx,ny,space[nx][ny]))

while(True):
    hq=[]
    heapq.heapify(hq)

    calcul()

    check=False

    while(hq):
        t_d,target_x,target_y,t_s=heapq.heappop(hq)

        if(t_s<baby_s):
            check=True
            break

    if(not check):
        print(time)
        break
    else:
        time+=t_d
        space[target_x][target_y]=0

        baby_x=target_x
        baby_y=target_y

        count-=1
        if(count==0):
            baby_s+=1
            count=baby_s
import sys
from collections import defaultdict,deque
import heapq

input=sys.stdin.readline

N=int(input())
space=[list(map(int,input().split())) for _ in range(N)]

time=0

dx=[0,0,-1,1]
dy=[1,-1,0,0]

bs_x=0
bs_y=0
size=2
count=0

for i in range(N):
    for j in range(N):
        if(space[i][j]==9):
            bs_x=i
            bs_y=j
            space[i][j]=0


def find(x,y,size):
    global prey
    global visited

    dequee=deque()
    dequee.append((x,y,0))

    while(dequee):
        cx,cy,cost=dequee.popleft()

        if(space[cx][cy]!=0 and space[cx][cy]<size):
            heapq.heappush(prey,(cost,cx,cy))

        for i in range(4):
            nx=cx+dx[i]
            ny=cy+dy[i]

            if(0<=nx<N and 0<=ny<N and space[nx][ny]<=size and not visited[nx][ny]):
                visited[nx][ny]=True
                dequee.append((nx,ny,cost+1))


while(True):
    prey=[]
    visited=[[False for _ in range(N)] for _ in range(N)]
    visited[bs_x][bs_y]=True

    heapq.heapify(prey)

    find(bs_x,bs_y,size)

    if(len(prey)==0):
        print(time)
        break
    else:
        target=heapq.heappop(prey)

        bs_x=target[1]
        bs_y=target[2]
        time+=target[0]
        count+=1

        #선택한 물고기 없애주기
        space[bs_x][bs_y]=0

        if(count==size):
            size+=1
            count=0
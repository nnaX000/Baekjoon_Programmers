import sys
import heapq

# 운영진은 (1,1)에 있음. (N,M)으로 이동해야 함.

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
miro=[]
for i in range(M):
    miro.append(list(map(int,sys.stdin.readline().rstrip())))

dist=[[-1 for i in range(N)] for j in range(M)]

if(miro[0][0]==0):
    dist[0][0]=0
else:
    dist[0][0]=1

dx=[-1,1,0,0]
dy=[0,0,-1,1]

heap=[]
heapq.heappush(heap,[0 if(miro[0][0]==0) else 1,0,0]) #[깨부순 벽 수, 위치x, 위치y]

while(heap):
    wall,x,y=heapq.heappop(heap)

    if(x==M-1 and y==N-1):
        print(wall)
        break

    for i in range(4):
        if(0<=x+dx[i]<M and 0<=y+dy[i]<N and dist[x+dx[i]][y+dy[i]]==-1):
            if(miro[x+dx[i]][y+dy[i]]==1):
                dist[x+dx[i]][y+dy[i]]=wall+1
                heapq.heappush(heap,[wall+1,x+dx[i],y+dy[i]])
            else:
                dist[x+dx[i]][y+dy[i]]=wall
                heapq.heappush(heap,[wall,x+dx[i],y+dy[i]])
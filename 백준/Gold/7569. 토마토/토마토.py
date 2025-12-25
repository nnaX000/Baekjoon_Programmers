import sys
from collections import deque

M,N,H=map(int,sys.stdin.readline().rstrip().split(' '))
box=[]
dequee=deque()

dh=[0,0,0,0,-1,1]
dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]

empty=0

box=[[] for i in range(H)]

for i in range(H):
    for j in range(N):
        box[i].append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

visited=0
visited_set=set()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if(box[k][i][j]==-1):
                empty+=1
            elif(box[k][i][j]==1):
                dequee.append((k,i,j,0))
                visited_set.add((k,i,j))
                visited+=1

sum_value=H*N*M-empty

if(visited == sum_value):
    print(0)
    sys.exit(0)

while(dequee):
    h,x,y,count = dequee.popleft()

    for i in range(6):
        nh=h+dh[i]
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nh<H and 0<=nx<N and 0<=ny<M and box[nh][nx][ny]==0 and (nh,nx,ny) not in visited_set):
            visited+=1
            dequee.append((nh,nx,ny,count+1))
            visited_set.add((nh,nx,ny))

            if(visited == sum_value):
                print(count+1)
                sys.exit(0)

print(-1)
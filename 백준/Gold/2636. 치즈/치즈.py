import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

cheeze=[list(map(int,input().split())) for _ in range(N)]

#치즈가 없는 칸 0, 치즈가 있는칸 1
#치즈가 모두 녹아서 없어지는 데 걸리는 시간

dx=[-1,1,0,0]
dy=[0,0,-1,1]

c_count=0

for i in range(N):
    for j in range(M):
        if(cheeze[i][j]==1):
            c_count+=1

def drosion():
    global cheeze

    dq=deque()
    dq.append((0,0))
    visited=[[False for _ in range(M)] for _ in range(N)]

    while(dq):
        x,y=dq.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<N and 0<=ny<M and cheeze[nx][ny]!=1 and not visited[nx][ny]):
                visited[nx][ny]=True
                cheeze[nx][ny]=4 #외부공기
                dq.append((nx,ny))

d_count=0
last=0
time=0

while(d_count<c_count):
    drosion()

    change=[]

    for i in range(N):
        for j in range(M):
            if(cheeze[i][j]==1):
                check=False
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]

                    if(0<=nx<N and 0<=ny<M and cheeze[nx][ny]==4):
                        check=True
                        break

                if(check):
                    change.append([i,j])

    d_count+=len(change)
    time+=1
    if(d_count==c_count):
        last=len(change)

    for a,b in change:
        cheeze[a][b]=3    
        
print(time)
print(last)
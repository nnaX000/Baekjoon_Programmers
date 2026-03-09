import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())
cheeze=[list(map(int,input().split())) for _ in range(N)] #치즈 1, 치즈0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

c_n=0
out_x=0
out_y=0
cumulate=0
time=0

for i in range(N):
    for j in range(M):
        if(cheeze[i][j]==1):
            c_n+=1
        else:
            if(out_x==0 and out_y==0):
                out_x,out_y=i,j

if(c_n==0):
    print(0)
    sys.exit(0)

def air():
    global cheeze

    dq=deque()
    dq.append((out_x,out_y))
    cheeze[out_x][out_y]=-1

    visited=[[False for _ in range(M)] for _ in range(N)]

    while(dq):
        x,y=dq.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<N and 0<=ny<M and cheeze[nx][ny]!=1 and not visited[nx][ny]):
                visited[nx][ny]=True
                cheeze[nx][ny]=-1
                dq.append((nx,ny))

def vanish():
    global cheeze
    global cumulate

    change=[]

    for i in range(N):
        for j in range(M):

            if(cheeze[i][j]==1):
                count=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]

                    if(0<=nx<N and 0<=ny<M and cheeze[nx][ny]==-1):
                        count+=1
                
                if(count>1):
                    change.append([i,j])
                    cumulate+=1

    for a,b in change:
        cheeze[a][b]=0

while(True):
    air()
    vanish()
    time+=1

    if(cumulate==c_n):
        print(time)
        break
import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

campus=[list(input().rstrip()) for _ in range(N)]

do_x=0
do_y=0

for i in range(N):
    for j in range(M):
        if(campus[i][j]=="I"):
            do_x,do_y=i,j

dx=[-1,1,0,0]
dy=[0,0,-1,1]

q=deque()
q.append((do_x,do_y))

answer=0

while(q):
    x,y=q.popleft()

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<M and campus[nx][ny]!="X"):
            if(campus[nx][ny]=="P"):
                answer+=1
            campus[nx][ny]="X"
            q.append((nx,ny))

print(answer if answer!=0 else "TT")
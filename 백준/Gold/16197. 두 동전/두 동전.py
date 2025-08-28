import sys
from collections import deque

sys.setrecursionlimit(10**6)

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

board=[]

dequee=deque()

for i in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

# o : 동전
# . : 빈칸
# # : 벽

dx=[-1,1,0,0]
dy=[0,0,-1,1]

min_value=10000000

visited=set()

inix_1=-2
inix_2=-2
iniy_1=-2
iniy_2=-2

for i in range(N):
    for j in range(M):
        if(board[i][j]=="o"):
            if(inix_1==-2):
                inix_1=i
                iniy_1=j
            else:
                inix_2=i
                iniy_2=j
                break

visited.add((inix_1,iniy_1,inix_2,iniy_2))
visited.add((inix_2,iniy_2,inix_1,iniy_1))

dequee.append([inix_1,iniy_1,inix_2,iniy_2,0])

while(dequee):
    x_1,y_1,x_2,y_2,cost = dequee.popleft()

    for i in range(4):
        nx_1=x_1+dx[i]
        nx_2=x_2+dx[i]
        ny_1=y_1+dy[i]
        ny_2=y_2+dy[i]

        out_1=not(0<=nx_1<N and 0<=ny_1<M)
        out_2=not(0<=nx_2<N and 0<=ny_2<M)

        #둘다 out된 경우
        if(out_1 and out_2):
            continue
        
        #하나만 아웃된 경우-1
        if(out_1):
            if(not out_2):
                min_value=min(min_value,cost+1)
                continue

        #하나만 아웃된 경우-2
        if(out_2):
            if(not out_1):
                min_value=min(min_value,cost+1)
                continue
        
        #둘 다 보드 안에 있는 경우
        if(board[nx_1][ny_1]=="#"):
            nx_1=x_1
            ny_1=y_1
        
        if(board[nx_2][ny_2]=="#"):
            nx_2=x_2
            ny_2=y_2

        if((nx_1,ny_1,nx_2,ny_2)==(x_1,y_1,x_2,y_2)):
            continue

        if((nx_1,ny_1,nx_2,ny_2) not in visited and cost+1<10):
            visited.add((nx_1,ny_1,nx_2,ny_2))
            visited.add((nx_2,ny_2,nx_1,ny_1))
            dequee.append([nx_1,ny_1,nx_2,ny_2,cost+1])

if(min_value==10000000):
    print(-1)
else:
    print(min_value)
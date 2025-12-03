import sys
from collections import deque

N,M,fuel=map(int,sys.stdin.readline().rstrip().split(' '))

#최단거리 짧은 승객을 고르되 여러명이면 행번호 가장 작은 승객, 그것도 여러명이면 열 번호가 가장 작은 승객

board=[]
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
#0은 빈칸, 1은 벽

for i in range(N):
    for j in range(N):
        if(board[i][j]==1):
            board[i][j]=1000 #벽이 1000

current_x,current_y=map(int,sys.stdin.readline().rstrip().split(' '))
current_x-=1
current_y-=1

dx=[-1,0,1,0]
dy=[0,-1,0,1]

ride=set()
person=[]
path=[]

for i in range(M):
    tmp=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    person.append(tmp)
    board[tmp[0]-1][tmp[1]-1]=i+1

#각 출발지에서 도착지까지 최단거리 구하기
for i in range(M):
    dequee=deque()
    dequee.append((person[i][0]-1,person[i][1]-1,0))
    visited=[[False for j in range(N)] for k in range(N)]
    check=False

    while(dequee):
        x,y,cost=dequee.popleft()

        if(x==person[i][2]-1 and y==person[i][3]-1):
            path.append(cost)
            check=True
            break

        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]

            if(0<=nx<N and 0<=ny<N and board[nx][ny]!=1000 and not visited[nx][ny]):
                visited[nx][ny]=True
                dequee.append((nx,ny,cost+1))

    if(not check):
        print(-1)
        sys.exit(0)

#현재 위치에서 갈 수 있는 최단 손님 계산하기
for i in range(M):
    dequee=deque()
    dequee.append((current_x,current_y,0))
    visited=[[False for j in range(N)] for k in range(N)]
    check=False
    min_value=float('inf')
    candi=[]

    #태우러 갈 사람 찾기
    while(dequee):
        x,y,cost=dequee.popleft()

        if(1<=board[x][y]<=400 and board[x][y] not in ride):
            check=True
            
            if(min_value>cost):
                min_value=cost
                candi=[]
                candi.append([x,y])
            elif(min_value==cost):
                candi.append([x,y])
            
        
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]

            if(0<=nx<N and 0<=ny<N and board[nx][ny]!=1000 and not visited[nx][ny]):
                visited[nx][ny]=True
                dequee.append((nx,ny,cost+1))

    if(not check):
        print(-1)
        sys.exit(0)

    s_candi=sorted(candi,key=lambda x:x[1])
    s_candi=sorted(s_candi,key=lambda x:x[0])

    sum_value=min_value+path[board[s_candi[0][0]][s_candi[0][1]]-1]

    if(sum_value>fuel):
        print(-1)
        sys.exit(0)
    else:
        current_x=person[board[s_candi[0][0]][s_candi[0][1]]-1][2]-1
        current_y=person[board[s_candi[0][0]][s_candi[0][1]]-1][3]-1

        fuel-=sum_value
        fuel+=path[board[s_candi[0][0]][s_candi[0][1]]-1]*2
        ride.add(board[s_candi[0][0]][s_candi[0][1]])

print(fuel)
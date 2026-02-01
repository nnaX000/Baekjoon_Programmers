import sys
from collections import defaultdict,deque

input=sys.stdin.readline

# 가장 처음에 주사위의 이동 방향은 동쪽

N,M,K=map(int,input().split()) # 세로, 가로, 이동하는 횟수
dice = [1, 6, 4, 3, 2, 5] # 뚜껑, 바닥, 왼쪽, 오른쪽, 위, 아래

# A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
# A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
# A = B인 경우 이동 방향에 변화는 없다.

board=[list(map(int,input().split())) for _ in range(N)]

c_x=0
c_y=0
c_d=1

di=defaultdict(list) # 동 : 1 / 서 : 2 / 남 : 3 / 북 : 4
di[1]=[3,4]
di[2]=[4,3]
di[3]=[2,1]
di[4]=[1,2]

reverse=defaultdict(list)
reverse[1]=2
reverse[2]=1
reverse[3]=4
reverse[4]=3

dx=[0,0,1,-1]
dy=[1,-1,0,0]

answer=0

def bfs(x,y,stand):
    global count
    global visited
    
    dequee=deque()
    dequee.append((x,y))

    while(dequee):
        x,y=dequee.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<N and 0<=ny<M and board[nx][ny]==stand and not visited[nx][ny]):
                visited[nx][ny]=True
                dequee.append((nx,ny))
                count+=1


for i in range(K):
    if(c_d==1): # 동
        dice[0], dice[3], dice[1], dice[2] = dice[2], dice[0], dice[3], dice[1]

        c_x+=dx[c_d-1]
        c_y+=dy[c_d-1]
    elif(c_d==2): # 서
        dice[0], dice[2], dice[1], dice[3] = dice[3], dice[0], dice[2], dice[1]

        c_x+=dx[c_d-1]
        c_y+=dy[c_d-1]
    elif(c_d==3): # 남
        dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]

        c_x+=dx[c_d-1]
        c_y+=dy[c_d-1]
    else: # 북
        dice[0], dice[4], dice[1], dice[5] = dice[5], dice[0], dice[4], dice[1]

        c_x+=dx[c_d-1]
        c_y+=dy[c_d-1]


    if(not(0<=c_x<N and 0<=c_y<M)):
        c_x-=dx[c_d-1]
        c_y-=dy[c_d-1]
        c_d=reverse[c_d]

        if(c_d==1): # 동
             dice[0], dice[3], dice[1], dice[2] = dice[2], dice[0], dice[3], dice[1]
             dice[0], dice[3], dice[1], dice[2] = dice[2], dice[0], dice[3], dice[1]
        elif(c_d==2): # 서
            dice[0], dice[2], dice[1], dice[3] = dice[3], dice[0], dice[2], dice[1]
            dice[0], dice[2], dice[1], dice[3] = dice[3], dice[0], dice[2], dice[1]
        elif(c_d==3): # 남
            dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]
            dice[0], dice[5], dice[1], dice[4] = dice[4], dice[0], dice[5], dice[1]
        else: # 북
            dice[0], dice[4], dice[1], dice[5] = dice[5], dice[0], dice[4], dice[1]
            dice[0], dice[4], dice[1], dice[5] = dice[5], dice[0], dice[4], dice[1]

        c_x+=dx[c_d-1]
        c_y+=dy[c_d-1]

    #print("ㅇㅇㅇ",c_d,board[c_x][c_y],dice[1])

    if(board[c_x][c_y]<dice[1]):
        c_d=di[c_d][0]
    elif(board[c_x][c_y]>dice[1]):
        c_d=di[c_d][1]

    count=1
    visited=[[False for _ in range(M)] for _ in range(N)]
    visited[c_x][c_y]=True

    bfs(c_x,c_y,board[c_x][c_y])

    answer+=(board[c_x][c_y]*count)
    #print(answer,c_d,c_x,c_y)

print(answer)
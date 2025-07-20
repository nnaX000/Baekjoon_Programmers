import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

r,c,d=map(int,sys.stdin.readline().rstrip().split(' '))# r,c가 현재위치/d는 방향

room=[]

answer=0

move=False

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(N):
    room.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

while(True):
    move=False

    if(room[r][c]==0):
        room[r][c]=2
        answer+=1

    for i in range(4):

        d-=1
        if(d<0):
            d=3
            
        if(0<=r+dx[d]<N and 0<=c+dy[d]<M and room[r+dx[d]][c+dy[d]]==0):
            r+=dx[d]
            c+=dy[d]
            move=True
            break

    if(not move):
        if(0<=r+dx[(d+2)%4]<N and 0<=c+dy[(d+2)%4]<M and room[r+dx[(d+2)%4]][c+dy[(d+2)%4]]!=1):
            r+=dx[(d+2)%4]
            c+=dy[(d+2)%4]
        else:
            break

print(answer)
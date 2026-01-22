import sys

input=sys.stdin.readline

R,C,T=map(int,input().split())

#공청기 설치된 곳이 -1
#확산되는 양은 좌표값//5
#남은 미세먼지 양은 좌표값 - (좌표값//5)*확산된 방향 개수

room=[list(map(int,input().split())) for _ in range(R)]

air=[]#공청기 위치
air_range=[]
air_order=[[3,0,2,1],[3,1,2,0]]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(R):
    if(room[i][0]==-1):
        air.append([i,0])

for i in range(2):
    x=air[i][0]
    y=air[i][1]
    tmp=[]

    for j in range(4):
        while(True):
            x+=dx[air_order[i][j]]
            y+=dy[air_order[i][j]]

            if(0<=x<R and 0<=y<C):
                if([x,y]!=[air[i][0],air[i][1]]):
                    tmp.append([x,y])
                else:
                    break
            else:
                x-=dx[air_order[i][j]]
                y-=dy[air_order[i][j]]
                break

    air_range.append(tmp)


for t in range(T):
    tmp=[[0 for _ in range(C)] for _ in range(R)]

    for x,y in air:
        tmp[x][y]=-1

    #미세먼지 퍼뜨리기
    for i in range(R):
        for j in range(C):
            if(room[i][j]>0):
                count=0
                portion=room[i][j]//5
                for k in range(4):
                    if(0<=i+dx[k]<R and 0<=j+dy[k]<C and room[i+dx[k]][j+dy[k]]!=-1):
                        count+=1
                        tmp[i+dx[k]][j+dy[k]]+=portion
                tmp[i][j]+=room[i][j]-(portion*count)

    #공청기로 밀기
    for i in range(2):
        s_x,s_y=air_range[i][0][0],air_range[i][0][1]
        stand=tmp[s_x][s_y]

        tmp[s_x][s_y]=0

        for j in range(1,len(air_range[i])):
            next_x=air_range[i][j][0]
            next_y=air_range[i][j][1]
            next=tmp[next_x][next_y]

            tmp[next_x][next_y]=stand #밀기
            stand=next

    room=[i[:] for i in tmp]

answer=sum(sum(i) for i in room)+2
print(answer)
import sys
from collections import defaultdict

input=sys.stdin.readline

R,C,M=map(int,input().split()) # 격자판 크기 행, 열 / 상어의 수

#낚시왕은 행초만큼 이동.

beach=[[(0,0,0) for _ in range(C)] for _ in range(R)]
answer=0

for i in range(M):
    r,c,s,d,z=map(int,input().split())

    beach[r-1][c-1]=(s,d,z) # 속력, 이동방향, 크기

# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽

directions=defaultdict(int)

directions[1]=2
directions[2]=1
directions[3]=4
directions[4]=3

dx=[-1,1,0,0]
dy=[0,0,1,-1]

def move():
    global beach
    candi=defaultdict(tuple)

    for i in range(R):
        for j in range(C):
            if(beach[i][j]!=(0,0,0)):
                speed=beach[i][j][0]
                di=beach[i][j][1]
                size=beach[i][j][2]

                if(di==1): # 위
                    ram=R-(R-i) # 4-(4-1)=1

                    if(ram>=speed):
                        nx=i+(dx[0]*speed)
                        ny=j+(dy[0]*speed)
                        nd=di
                    else:
                        tmp=speed-ram #1
                        mok=tmp//(R-1) #0
                        r=tmp%(R-1) #1
                        ny=j

                        if mok%2==1:
                            nx=R-1+dx[directions[2]-1]*r
                            nd=1
                        else:
                            nx=dx[directions[1]-1]*r
                            nd=2
                        
                elif(di==2):
                    ram=R-i-1 #4-0-1=3

                    if(ram>=speed):
                        nx=i+(dx[1]*speed)
                        ny=j+(dy[1]*speed)
                        nd=di
                    else:
                        tmp=speed-ram #2
                        mok=tmp//(R-1) #0
                        r=tmp%(R-1) #2
                        ny=j

                        if mok%2==1:
                            nx=dx[directions[1]-1]*r
                            nd=2
                        else:
                            nx=R-1+dx[directions[2]-1]*r
                            nd=1
                elif(di==3):
                    ram=C-j-1

                    if(ram>=speed):
                        nx=i+(dx[2]*speed)
                        ny=j+(dy[2]*speed)
                        nd=di
                    else:
                        tmp=speed-ram #1
                        mok=tmp//(C-1) #0
                        r=tmp%(C-1) #1
                        nx=i

                        if mok%2==1:
                            ny=dy[directions[4]-1]*r
                            nd=3
                        else:
                            ny=C-1+dy[directions[3]-1]*r
                            nd=4
                else:
                    ram=C-(C-j) # 6-(6-4)=4

                    if(ram>=speed):
                        nx=i+(dx[3]*speed)
                        ny=j+(dy[3]*speed)
                        nd=di
                    else:
                        tmp=speed-ram #4
                        mok=tmp//(C-1) #0
                        r=tmp%(C-1) #4
                        nx=i

                        if mok%2==1:
                            ny=C-1+dy[directions[3]-1]*r
                            nd=4
                        else:
                            ny=dy[directions[4]-1]*r
                            nd=3
                
                if((nx,ny) in candi):
                    if(candi[(nx,ny)][2]<size):
                        candi[(nx,ny)]=(speed,nd,size)
                else:
                    candi[(nx,ny)]=(speed,nd,size)
    
    beach=[[(0,0,0) for _ in range(C)] for _ in range(R)]

    #변경 사항 일괄 삽입
    for key,value in candi.items():
        nx,ny=key[0],key[1]
        speed,nd,size=value[0],value[1],value[2]

        beach[nx][ny]=(speed,nd,size)

for i in range(C):

    # 낚시왕이 있는 열에 있는 가장 땅에 가까운 물고기 잡아먹기
    for j in range(R):
        if(beach[j][i]!=(0,0,0)):
            answer+=beach[j][i][2]
            beach[j][i]=(0,0,0)
            break

    move()

print(answer)
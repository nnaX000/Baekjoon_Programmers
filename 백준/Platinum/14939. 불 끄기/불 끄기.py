import sys
from itertools import product

input=sys.stdin.readline

bulb=[list(input().rstrip()) for _ in range(10)]
n_bulb=[i[:] for i in bulb]

candi=[0,1] #그대로, 바꾸기

answer=float('inf')

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for cases in product(candi,repeat=10):
    result=0
    n_bulb=[i[:] for i in bulb]

    #첫째줄 완탐
    for idx,i in enumerate(cases):
        if(i==1):
            result+=1

            if(n_bulb[0][idx]=="#"):
                n_bulb[0][idx]="O"
            else:
                n_bulb[0][idx]="#"

            for k in range(4):
                nx=0+dx[k]
                ny=idx+dy[k]

                if(0<=nx<10 and 0<=ny<10):
                    if(n_bulb[nx][ny]=="#"):
                        n_bulb[nx][ny]="O"
                    else:
                        n_bulb[nx][ny]="#"

    for i in range(1,10):
        for j in range(10):
            if(n_bulb[i-1][j]!="#"):
                result+=1

                #센터 바꿈
                if(n_bulb[i][j]=="#"):
                    n_bulb[i][j]="O"
                else:
                    n_bulb[i][j]="#"

                #상하좌우
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]

                    if(0<=nx<10 and 0<=ny<10):
                        if(n_bulb[nx][ny]=="#"):
                            n_bulb[nx][ny]="O"
                        else:
                            n_bulb[nx][ny]="#"

    check=False
    for i in range(10):
        if(n_bulb[9][i]!="#"):
            check=True
            break

    if(not check):
        answer=min(answer,result)
        
print(answer if answer!=float('inf') else -1)
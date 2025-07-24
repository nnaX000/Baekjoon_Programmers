import sys
from collections import deque

#두 나라 인구수 차이가 L명이상 R명 이하라면 국경선을 하루 연다
#연합을 이루고 있는 각 칸 인구수는 연합인구수/연합을 이루는 칸개수. 소수점은 버린다.
#다하면 연합을 해체하고 모든 국경선 닫음
#인구이동이 며칠동안 발생?

N,L,R=map(int,sys.stdin.readline().rstrip().split(' '))

earth=[]
result=[]

time=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(N):
    earth.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

#BFS의 결과물로 좌표 리턴
def bfs(dequee,result,sum_value,visited):
    while(dequee):
        tmp=dequee.popleft()
        x=tmp[0]
        y=tmp[1]
        for i in range(4):
            if(0<=x+dx[i]<N and 0<=y+dy[i]<N and not visited[x+dx[i]][y+dy[i]]):
                if(L<=abs(earth[x][y]-earth[x+dx[i]][y+dy[i]])<=R):
                    result.append([x+dx[i],y+dy[i]])
                    dequee.append([x+dx[i],y+dy[i]])
                    visited[x+dx[i]][y+dy[i]]=True
                    sum_value+=earth[x+dx[i]][y+dy[i]]

    return result,sum_value


while(True):
    visited=[[False for i in range(N)]for j in range(N)]
    open=False
    for i in range(N):
        for j in range(N):
            if(not visited[i][j]):
                result=[]
                sum_value=earth[i][j]
                dequee=deque()
                dequee.append([i,j])
                visited[i][j]=True
                result.append([i,j])
                result,total_value=bfs(dequee,result,sum_value,visited)
                if(len(result)>1):
                    open=True
                    new_value=total_value//len(result)
                    for k in result:
                        earth[k[0]][k[1]]=new_value

    if(not open):
        break
    else:
        time+=1

print(time)
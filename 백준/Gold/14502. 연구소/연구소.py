import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

maps=[list(map(int,input().split())) for _ in range(N)]

#0이 빈칸, 1이 벽, 2가 바이러스
#벽을 세개만 세워야 함.

vacant=[]
virus=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=float('-inf')

for i in range(N):
    for j in range(M):
        if(maps[i][j]==0):
            vacant.append([i,j])
        elif(maps[i][j]==2):
            virus.append([i,j])

candi=[]
# 벽 세울 경우의 수 구하기
def dfs(start,arr):
    global candi

    if(len(arr)==3):
        candi.append(arr[:])
        return
    
    for i in range(start,len(vacant)):
        arr.append(vacant[i])
        dfs(i+1,arr)
        arr.pop()

dfs(0,[])

#바이러스 퍼져나가는 거 체크
def bfs():
    global maps_t
    global dequee

    while(dequee):
        x,y=dequee.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<N and 0<=ny<M and maps_t[nx][ny]==0):
                maps_t[nx][ny]=2
                dequee.append((nx,ny))


for i in range(len(candi)):
    maps_t=[j[:] for j in maps]

    # 벽 세우기
    for j in range(len(candi[i])):
        x,y=candi[i][j][0],candi[i][j][1]
        maps_t[x][y]=1
    
    dequee=deque(virus)

    bfs()

    tmp=0
    for j in range(N):
        for k in range(M):
            if(maps_t[j][k]==0):
                tmp+=1

    answer=max(answer,tmp)

print(answer)
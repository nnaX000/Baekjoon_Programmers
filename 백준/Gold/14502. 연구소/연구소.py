import sys
from itertools import combinations
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(N)]

answer=float(('-inf'))

vacant=[]
virus=[]
wall=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    global count
    global dequee
    global visited

    while(dequee):
        x,y=dequee.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if(0<=nx<N and 0<=ny<M and maps[nx][ny]==0 and (nx,ny) not in visited):
                visited.add((nx,ny))
                count+=1
                dequee.append((nx,ny))

for i in range(N):
    for j in range(M):
        if(maps[i][j]==0):
            vacant.append([i,j])
        elif(maps[i][j]==2):
            virus.append([i,j])
        else:
            wall.append([i,j])

for i in combinations(vacant,3):
    for a,b in i:
        maps[a][b]=1

    count=0
    dequee=deque(virus)
    visited=set()

    bfs()

    answer=max(answer,N*M-len(virus)-len(wall)-count-3)

    for a,b in i:
        maps[a][b]=0

print(answer)
import sys
from copy import deepcopy

N,K=map(int,sys.stdin.readline().rstrip().split(' '))

virus=[list(map(int,sys.stdin.readline().rstrip().split(' '))) for i in range(N)]
S,x,y=map(int,sys.stdin.readline().rstrip().split(' '))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

candi=[]

for i in range(N):
    for j in range(N):
        if(virus[i][j]!=0):
            candi.append((i,j))

for i in range(S):
    visited=set()
    for j,k in candi:
        if(virus[j][k]!=0 and (j,k) not in visited):
            for l in range(4):
                n_x=j+dx[l]
                n_y=k+dy[l]

                if(0<=n_x<N and 0<=n_y<N):
                    if(virus[n_x][n_y]!=0 and virus[n_x][n_y]>virus[j][k] and (n_x,n_y) in visited):
                        visited.add((n_x,n_y))
                        virus[n_x][n_y]=virus[j][k]
                    elif(virus[n_x][n_y]==0):
                        visited.add((n_x,n_y))
                        virus[n_x][n_y]=virus[j][k]

    candi=list(deepcopy(visited))

print(virus[x-1][y-1])
import sys

sys.setrecursionlimit(10**6)

def dfs(x,y):
    global cabbage

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<M and 0<=ny<N and cabbage[nx][ny]==1):
            cabbage[nx][ny]=0
            dfs(nx,ny)

T=int(sys.stdin.readline().rstrip())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(T):

    answer=0
    M,N,K=map(int,sys.stdin.readline().rstrip().split(' '))
    cabbage=[[0 for i in range(N)] for j in range(M)]

    for j in range(K):
        a,b=map(int,sys.stdin.readline().rstrip().split(' '))
        cabbage[a][b]=1

    for j in range(M):
        for k in range(N):
            if(cabbage[j][k]==1):
                cabbage[j][k]=0
                answer+=1
                dfs(j,k)

    print(answer)
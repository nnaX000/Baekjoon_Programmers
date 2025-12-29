import sys

input=sys.stdin.readline

N=int(input())

maps=[list(map(int,input().rstrip())) for _ in range(N)]

cost=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=[]

def dfs(x,y):
    global cost

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<N and maps[nx][ny]==1):
            maps[nx][ny]=0
            dfs(nx,ny)
            cost+=1

for i in range(N):
    for j in range(N):
        if(maps[i][j]==1):
            maps[i][j]=0
            cost=1
            dfs(i,j)
            answer.append(cost)

answer.sort()
print(len(answer))
for i in answer:
    print(i)
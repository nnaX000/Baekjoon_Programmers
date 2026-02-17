import sys

input=sys.stdin.readline

N=int(input())

maps=[list(map(int,input().rstrip())) for _ in range(N)]
visited=[[False for _ in range(N)] for _ in range(N)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=[]

def dfs(x,y):
    global visited
    global count

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<N and maps[nx][ny]==1 and not visited[nx][ny]):
            visited[nx][ny]=True
            count+=1
            dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if(maps[i][j]==1 and not visited[i][j]):
            visited[i][j]=True
            count=1
            dfs(i,j)
            answer.append(count)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
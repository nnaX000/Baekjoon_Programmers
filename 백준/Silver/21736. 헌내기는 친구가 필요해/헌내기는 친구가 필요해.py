import sys

sys.setrecursionlimit(10**6)

input=sys.stdin.readline

N,M=map(int,input().split())

campus=[list(input()) for _ in range(N)]

# O는 빈 공간, X는 벽, I는 도연이, P는 사람
visited=[[False for _ in range(M)] for _ in range(N)]
d_x=0
d_y=0
answer=0

for i in range(N):
    for j in range(M):
        if(campus[i][j]=="I"):
            d_x=i
            d_y=j
            campus[i][j]="O"
            break

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global answer

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<M and campus[nx][ny]!="X" and not visited[nx][ny]):
            visited[nx][ny]=True
            if(campus[nx][ny]=="P"):
                answer+=1
            dfs(nx,ny)

dfs(d_x,d_y)
print(answer if answer!=0 else "TT")
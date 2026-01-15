import sys

input=sys.stdin.readline

R,C=map(int,input().split())
board=[list(input().rstrip()) for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=float('-inf')

def dfs(x,y,visited,cost):
    global answer

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<R and 0<=ny<C and not visited[ord(board[nx][ny])-65]):
            visited[ord(board[nx][ny])-65]=True
            answer=max(answer,cost+1)
            dfs(nx,ny,visited,cost+1)
            visited[ord(board[nx][ny])-65]=False


visited=[False for _ in range(26)]
visited[ord(board[0][0])-65]=True
dfs(0,0,visited,1) #x,y,visited

print(answer if answer!=float('-inf') else 1)
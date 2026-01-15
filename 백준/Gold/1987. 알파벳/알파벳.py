import sys
from collections import defaultdict

input=sys.stdin.readline

R,C=map(int,input().split())
board=[list(input().rstrip()) for _ in range(R)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
answer=float('-inf')

visited_state=set()

def dfs(x,y,visited,cost):
    global answer

    if (x,y,visited) in visited_state:
        return
    visited_state.add((x,y,visited))

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<R and 0<=ny<C):
            bit = 1 << (ord(board[nx][ny])-65)
            if(not bit & visited):
                answer=max(answer,cost+1)
                dfs(nx,ny,visited|bit,cost+1)

visited = 1 << (ord(board[0][0])-65)
dfs(0,0,visited,1) #x,y,visited

print(answer if answer!=float('-inf') else 1)
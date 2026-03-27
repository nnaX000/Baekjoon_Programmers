import sys

sys.setrecursionlimit(10**6)

input=sys.stdin.readline

n,m=map(int,input().split())

picture=[list(map(int,input().split())) for _ in range(n)]

# 0은 색칠이 안된 부분, 1은 색칠이 된 부분

visited=[[False for _ in range(m)] for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

m_num=float('-inf')
answer=0

def dfs(x,y):
    global visited
    global count

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<n and 0<=ny<m and picture[nx][ny]==1 and not visited[nx][ny]):
            visited[nx][ny]=True
            count+=1
            dfs(nx,ny)

for i in range(n):
    for j in range(m):
        if(picture[i][j]==1 and not visited[i][j]):
            count=1
            visited[i][j]=True
            answer+=1
            dfs(i,j)
            m_num=max(m_num,count)

print(answer)
print(m_num if m_num!=float('-inf') else 0)
import sys

input=sys.stdin.readline

N,M=map(int,input().rstrip().split(' '))
paper=[]

for i in range(N):
    paper.append(list(map(int,input().rstrip().split(' '))))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[False for k in range(M)] for l in range(N)]

max_value=float('-inf')

def dfs(x,y,cost,visited,num):
    global max_value

    if(num==4):
        max_value=max(max_value,cost)
        return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<M and not visited[nx][ny]):
            visited[nx][ny]=True
            dfs(nx,ny,cost+paper[nx][ny],visited,num+1)
            visited[nx][ny]=False

for i in range(N):
    for j in range(M):
        visited[i][j]=True
        dfs(i,j,paper[i][j],visited,1)
        visited[i][j]=False

for i in range(N):
    for j in range(M):
        candi=[]
        for k in range(4):
            if(0<=i+dx[k]<N and 0<=j+dy[k]<M):
                candi.append(paper[i+dx[k]][j+dy[k]])
        
        if(len(candi)>=3):
            candi.sort(reverse=True)
            max_value=max(max_value,paper[i][j]+sum(candi[:3]))

print(max_value)
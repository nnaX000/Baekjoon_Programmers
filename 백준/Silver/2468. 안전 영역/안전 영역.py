import sys

sys.setrecursionlimit(10**7)

N=int(sys.stdin.readline().rstrip())
max_value=float('-inf')
answer=float('-inf')
visited=[[False for i in range(N)]for j in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

array=[]
for i in range(N):
    tmp=list(map(int,sys.stdin.readline().split(' ')))
    if(max(tmp)>max_value):
        max_value=max(tmp)
    array.append(tmp)

def dfs(x,y,limit):
    global visited

    for i in range(4):
        n_x=x+dx[i]
        n_y=y+dy[i]

        if(0<=n_x<N and 0<=n_y<N and array[n_x][n_y]>limit and not visited[n_x][n_y]):
            visited[n_x][n_y]=True
            dfs(n_x,n_y,limit)

for i in range(0,max_value+1):
    visited=[[False for k in range(N)]for j in range(N)]
    result=0
    for j in range(N):
        for k in range(N):
            if(array[j][k]>i and not visited[j][k]):
                visited[j][k]=True
                dfs(j,k,i)
                result+=1

    answer=max(result,answer)

print(answer)
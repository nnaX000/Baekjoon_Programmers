import sys
import copy

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
max_value=float('-inf')

array=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[False for k in range(M)] for l in range(N)]

for i in range(N):
    array.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))

def dfs(x,y,visited,sum_value,count):
    global max_value

    if(count==4):
        max_value=max(max_value,sum_value)
        return
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=nx<N and 0<=ny<M and not visited[nx][ny]):
            visited[nx][ny]=True
            dfs(nx,ny,visited,sum_value+array[nx][ny],count+1)
            visited[nx][ny]=False

for i in range(N):
    for j in range(M):
        visited[i][j]=True
        dfs(i,j,visited,array[i][j],1)
        visited[i][j]=False

#가로
for i in range(N):
    for j in range(M-3+1):
        sum_value=0
        sum_value+=array[i][j]+array[i][j+1]+array[i][j+2]

        if(i==0):
            sum_value+=array[i+1][j+1]
            max_value=max(sum_value,max_value)
        elif(i==N-1):
            sum_value+=array[i-1][j+1]
            max_value=max(sum_value,max_value)
        else:
            sum_value+=array[i+1][j+1]
            max_value=max(sum_value,max_value)
            sum_value-=array[i+1][j+1]
            sum_value+=array[i-1][j+1]
            max_value=max(sum_value,max_value)

#세로
for i in range(M):
    for j in range(N-3+1):
        sum_value=0
        sum_value+=array[j][i]+array[j+1][i]+array[j+2][i]

        if(i==0):
            sum_value+=array[j+1][i+1]
            max_value=max(sum_value,max_value)
        elif(i==M-1):
            sum_value+=array[j+1][i-1]
            max_value=max(sum_value,max_value)
        else:
            sum_value+=array[j+1][i+1]
            max_value=max(sum_value,max_value)
            sum_value-=array[j+1][i+1]

            sum_value+=array[j+1][i-1]
            max_value=max(sum_value,max_value)

print(max_value)
import sys

sys.setrecursionlimit(10**6)

N=int(sys.stdin.readline().rstrip())

#빨강, 초록, 파랑
#적록색약은 근데 빨간색하고 초록색 차이를 거의 못 느낌

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def normal_dfs(x,y,color):
    global visited

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<N and not visited[nx][ny] and array[nx][ny]==color):
            visited[nx][ny]=True
            normal_dfs(nx,ny,color)

def dfs(x,y,color):
    global visited

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if(0<=nx<N and 0<=ny<N and not visited[nx][ny]):
            if(color=="R" or color=="G"):
                if(array[nx][ny]=="R" or array[nx][ny]=="G"):
                    visited[nx][ny]=True
                    dfs(nx,ny,color)
            else:
                if(color==array[nx][ny]):
                    visited[nx][ny]=True
                    dfs(nx,ny,color)

array=[]

for i in range(N):
    array.append(list(sys.stdin.readline().rstrip()))

visited=[[False for i in range(N)] for j in range(N)]
normal_answer=0

#적록색약이 아닌 사람
for i in range(N):
    for j in range(N):
        if(not visited[i][j]):
            visited[i][j]=True
            normal_dfs(i,j,array[i][j])
            normal_answer+=1

visited=[[False for i in range(N)] for j in range(N)]
answer=0

for i in range(N):
    for j in range(N):
        if(not visited[i][j]):
            visited[i][j]=True
            dfs(i,j,array[i][j])
            answer+=1

print(normal_answer,answer)
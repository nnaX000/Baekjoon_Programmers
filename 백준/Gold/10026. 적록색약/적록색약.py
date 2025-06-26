import sys
sys.setrecursionlimit(10**6)

N=int(input())
picture=[]
for i in range(N):
    row=input()
    temp=[]
    for j in row:
        temp.append(j)
    picture.append(temp)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

answer=0
yak_answer=0

visited=[[False for i in range(N)] for j in range(N)]
yak_visited=[[False for i in range(N)] for j in range(N)]

def dfs(x,y,color) :

    visited[x][y]=True
    
    for i in range(4):
        new_x=x+dx[i]
        new_y=y+dy[i]

        if(0<=new_x<N and 0<=new_y<N and not visited[new_x][new_y]):
            if(picture[new_x][new_y]==color):
                visited[new_x][new_y]=True
                dfs(new_x,new_y,color)


def yak_dfs(x,y,color) :

    yak_visited[x][y]=True
    
    for i in range(4):
        new_x=x+dx[i]
        new_y=y+dy[i]

        if(0<=new_x<N and 0<=new_y<N and not yak_visited[new_x][new_y]):
            if(picture[new_x][new_y]==color or (color == 'G' and picture[new_x][new_y]=='R') or (color == 'R' and picture[new_x][new_y]=='G')):
                yak_visited[new_x][new_y]=True
                yak_dfs(new_x,new_y,color)


for i in range(N):
    for j in range(N):
        if(not visited[i][j]):
            dfs(i,j,picture[i][j])
            answer+=1

for i in range(N):
    for j in range(N):
        if(not yak_visited[i][j]):
            yak_dfs(i,j,picture[i][j])
            yak_answer+=1

print(answer,yak_answer)


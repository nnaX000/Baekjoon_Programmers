import sys

N,M,K=map(int,sys.stdin.readline().rstrip().split(' '))
array=[]
for i in range(N):
    array.append(list(map(int,sys.stdin.readline().rstrip().split(' '))))
max_value=[float('-inf')]

dx=[0,0,-1,1]
dy=[1,-1,0,0]
tmp=[]
visited=[[False for i in range(M)]for j in range(N)]

def dfs(tmp,start_x,start_y,visited):
    global max_value

    if(len(tmp)==K):
        sum_value=sum([array[i][j] for i,j in tmp])
        if(sum_value>max_value[0]):
            max_value[0]=sum_value
        return
    
    for i in range(start_x,N):
        for j in range(start_y if i==start_x else 0,M):
            if(not visited[i][j]):
                tmp.append([i,j])
                visited[i][j]=True
                blocked=[]
                for k in range(4):
                    if(0<=i+dx[k]<N and 0<=j+dy[k]<M and not visited[i+dx[k]][j+dy[k]]):
                        blocked.append([i+dx[k],j+dy[k]])
                        visited[i+dx[k]][j+dy[k]]=True

                new_x,new_y=i,j+1
                if(new_y>=M):
                    new_y=0
                    new_x=i+1

                dfs(tmp,new_x,new_y,visited)

                tmp.pop()
                visited[i][j]=False
                for k in blocked:
                    visited[k[0]][k[1]]=False

dfs(tmp,0,0,visited)
print(max_value[0])
import sys

input=sys.stdin.readline

N,M=map(int,input().split()) # 유저수, 친구 관계 수

graph=[[1000000 for _ in range(N+1)] for i in range(N+1)]

sum_values=[]

for i in range(M):
    a,b=map(int,input().split())

    graph[a][b]=1
    graph[b][a]=1

for i in range(1,N+1):
    graph[i][i]=0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,N+1):
    sum_values.append(sum(graph[i]))

min_value=min(sum_values)

for i in range(N):
    if(sum_values[i]==min_value):
        print(i+1)
        break
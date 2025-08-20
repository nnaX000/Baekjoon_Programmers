import sys

sys.setrecursionlimit(10**6)

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
graph=[[] for i in range(N+1)]
answer=0

for i in range(M):
    a,b=map(int,sys.stdin.readline().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    for i in range(len(graph[start])):
        if(not visited[graph[start][i]]):
            visited[graph[start][i]]=True
            dfs(graph[start][i])

visited=[False for i in range(N+1)]

for i in range(1,N+1):
    if(not visited[i]):
        dfs(i)
        answer+=1

print(answer)
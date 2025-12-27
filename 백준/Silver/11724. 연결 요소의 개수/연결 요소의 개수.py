import sys

sys.setrecursionlimit(10**6)

input=sys.stdin.readline

N,M=map(int,input().split(' '))

edge=[[] for i in range(N+1)]
visited=[False for i in range(N+1)]

answer=0

def dfs(node):
    global visited

    for i in range(len(edge[node])):
        if(not visited[edge[node][i]]):
            visited[edge[node][i]]=True
            dfs(edge[node][i])

for i in range(M):
    a,b=map(int,input().rstrip().split(' '))

    edge[a].append(b)
    edge[b].append(a)

for i in range(1,N+1):
    if(not visited[i]):
        visited[i]=True
        dfs(i)
        answer+=1

print(answer)
import sys
from collections import deque

N,M,V=map(int,sys.stdin.readline().rstrip().split(' '))

graph=[[] for i in range(N+1)]

for i in range(M):
    a,b=map(int,sys.stdin.readline().rstrip().split(' '))

    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

visited=set()
visited.add(V)

answer=[V]

def dfs(x):
    global answer

    for i in range(len(graph[x])):
        if(graph[x][i] not in visited):
            visited.add(graph[x][i])
            answer.append(graph[x][i])
            dfs(graph[x][i])

dfs(V)
print(*answer)

answer=[]
dequee=deque()
dequee.append(V)

visited=set()
visited.add(V)

while(dequee):
    x=dequee.popleft()
    answer.append(x)

    for i in range(len(graph[x])):
        if(graph[x][i] not in visited):
            visited.add(graph[x][i])
            dequee.append(graph[x][i])

print(*answer)
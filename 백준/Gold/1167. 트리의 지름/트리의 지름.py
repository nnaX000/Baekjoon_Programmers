import sys
from collections import deque

input=sys.stdin.readline

V=int(input())
edges=[[] for _ in range(V+1)]

for i in range(V):
    tmp=list(map(int,input().split()))

    for j in range(1,len(tmp)-1,2):
        edges[tmp[0]].append([tmp[j],tmp[j+1]])
        edges[tmp[j]].append([tmp[0],tmp[j+1]])

def bfs(x):
    global visited

    dq=deque()
    dq.append((x,0))

    while(dq):
        a,cost=dq.popleft()

        for i in range(len(edges[a])):
            if(visited[edges[a][i][0]]==float('-inf')):
                visited[edges[a][i][0]]=cost+edges[a][i][1]
                dq.append((edges[a][i][0],cost+edges[a][i][1]))

visited=[float('-inf') for _ in range(V+1)]
visited[1]=0
bfs(1)
mv=max(visited)
d1=0

for i in range(len(visited)):
    if(visited[i]==mv):
        d1=i
        break

visited=[float('-inf') for _ in range(V+1)]
visited[d1]=0
bfs(d1)

print(max(visited))
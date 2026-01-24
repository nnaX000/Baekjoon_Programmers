import sys
from collections import deque

input=sys.stdin.readline

V=int(input())

tree=[[] for _ in range(V+1)]

for i in range(V):
    tmp=list(map(int,input().split()))
    key=tmp[0]

    for j in range(1,len(tmp)-1,2):
        tree[key].append([tmp[j],tmp[j+1]])

def bfs():
    global result
    global dequee

    while(dequee):
        n,cost=dequee.popleft()

        for i in range(len(tree[n])):
            if(not visited[tree[n][i][0]]):
                visited[tree[n][i][0]]=True
                result[tree[n][i][0]]=cost+tree[n][i][1]
                dequee.append((tree[n][i][0],cost+tree[n][i][1]))


result=[0 for _ in range(V+1)]
result[1]=0
visited=[False for _ in range(V+1)]
visited[1]=True
dequee=deque()
dequee.append((1,0))

bfs()
max_value=max(result)

op=0
for i in range(len(result)):
    if(result[i]==max_value):
        op=i
        break


result=[0 for _ in range(V+1)]
result[op]=0
visited=[False for _ in range(V+1)]
visited[op]=True
dequee=deque()
dequee.append((op,0))

bfs()
max_value=max(result)

print(max_value)
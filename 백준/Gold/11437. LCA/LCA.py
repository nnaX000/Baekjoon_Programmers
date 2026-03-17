import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
edges=[[] for _ in range(N+1)]
parent=[0 for _ in range(N+1)]
up=[[] for _ in range(N+1)]
answer=[]
parent[1]=-1
nxt=[0 for _ in range(N+1)]
nxt[1]=1

dq=deque()
dq.append(1)

for i in range(N-1):
    a,b=map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

#루트가 1
while(dq):
    x=dq.popleft()

    for i in range(len(edges[x])):
        if(parent[edges[x][i]]==0):
            parent[edges[x][i]]=x
            nxt[edges[x][i]]=nxt[x]+1
            dq.append(edges[x][i])

M=int(input())

for i in range(M):
    a,b=map(int,input().split())
    stand=set(up[a])

    while(nxt[a]<nxt[b]):
        b=parent[b]
    while(nxt[a]>nxt[b]):
        a=parent[a]

    while(a!=b):
        a=parent[a]
        b=parent[b]
    
    answer.append(a)

for i in answer:
    print(i)
import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

edges=[[] for _ in range(N+1)]
order=[]
dq=deque()

dq.append(1) #루트 삽입
parent=[0 for _ in range(N+1)]
parent[1]=-1

for i in range(N-1):
    u,v=map(int,input().split())
    edges[u].append(v)
    edges[v].append(u)

while(dq):
    x=dq.popleft()
    order.append(x)

    for i in range(len(edges[x])):
        if(parent[edges[x][i]]==0):
            parent[edges[x][i]]=x
            dq.append(edges[x][i])

dp=[[0,0] for _ in range(N+1)]

for i in reversed(order):
    dp[i][1]=1
    for j in range(len(edges[i])):
        if(parent[i]!=edges[i][j]):
            dp[i][0]+=dp[edges[i][j]][1]
            dp[i][1]+=min(dp[edges[i][j]][0],dp[edges[i][j]][1])

print(min(dp[1][0],dp[1][1]))
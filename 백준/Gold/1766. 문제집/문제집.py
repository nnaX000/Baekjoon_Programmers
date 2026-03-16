import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())

answer=[]

prev=[[] for _ in range(N+1)]
cnt=[0 for _ in range(N+1)]
visited=[False for _ in range(N+1)]

for i in range(M):
    A,B=map(int,input().split())
    prev[A].append(B)
    cnt[B]+=1

dq=deque()

for i in range(1,N+1):
    if(cnt[i]==0):
        dq.append(i)

while(dq):
    dq=deque(sorted(list(dq)))
    x=dq.popleft()
    answer.append(x)
    visited[x]=True

    for i in range(len(prev[x])):
        if(not visited[prev[x][i]]):
            cnt[prev[x][i]]-=1

            if(cnt[prev[x][i]]==0):
                dq.append(prev[x][i])

print(*answer)
import sys
from collections import deque

input=sys.stdin.readline

N,K=map(int,input().split())

dq=deque()
dq.append((N,0)) #현재위치, cost

visited=[False for _ in range(100001)]
visited[N]=True

while(dq):
    position,cost=dq.popleft()

    if(position==K):
        print(cost)
        sys.exit(0)

    if(0<=position*2<=100000 and not visited[position*2]):
        dq.append((position*2,cost+1))
        visited[position*2]=True

    if(0<=position+1<=100000 and not visited[position+1]):
        dq.append((position+1,cost+1))
        visited[position+1]=True

    if(0<=position-1<=100000 and not visited[position-1]):
        dq.append((position-1,cost+1))
        visited[position-1]=True
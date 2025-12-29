import sys
from collections import deque

dequee=deque()
input=sys.stdin.readline

N,K=map(int,input().split())
dequee.append((N,0)) # 현재위치, cost
visited=[False for i in range(100001)]

while(dequee):
    current,cost=dequee.popleft()

    if(current==K):
        print(cost)
        sys.exit(0)

    if(current-1>=0 and not visited[current-1]):
        visited[current-1]=True
        dequee.append((current-1,cost+1))
    
    if(current+1<100001 and not visited[current+1]):
        visited[current+1]=True
        dequee.append((current+1,cost+1))

    if(current*2<100001 and not visited[current*2]):
        visited[current*2]=True
        dequee.append((current*2,cost+1))
import sys
from collections import deque

input=sys.stdin.readline

N,K=map(int,input().split())

dequee=deque()
dequee.append((N,0))

visited=[False for _ in range(100001)]

while(dequee):
    pos,count=dequee.popleft()

    if(pos==K):
        print(count)
        sys.exit(0)

    if(pos*2<=100000 and not visited[pos*2]):
        visited[pos*2]=True
        dequee.append((pos*2,count))

    if(pos-1>=0 and not visited[pos-1]):
        visited[pos-1]=True
        dequee.append((pos-1,count+1))

    if(pos+1<=100000 and not visited[pos+1]):
        visited[pos+1]=True
        dequee.append((pos+1,count+1))
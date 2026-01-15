import sys
from collections import deque

input=sys.stdin.readline

N,K=map(int,input().split())

visited=[-1 for _ in range(100001)]
dequee=deque(())

answer=-1
method=0

def bfs(x,cost):
    global answer
    global method

    dequee.append((x,cost))

    while(dequee):
        c_x,t=dequee.popleft()

        if(answer!=-1 and t>answer):
            continue

        if(c_x==K):
            if(answer==-1):
                answer=t
                method+=1
            else:
                if(t==answer):
                    method+=1
        else:
            visited[c_x]=t

        if(0<=c_x-1<=100000 and visited[c_x-1]==-1):
            dequee.append((c_x-1,t+1))
        if(0<=c_x+1<=100000 and visited[c_x+1]==-1):
            dequee.append((c_x+1,t+1))
        if(0<=c_x*2<=100000 and visited[c_x*2]==-1):
            dequee.append((c_x*2,t+1))

visited[N]=0
bfs(N,0)

print(answer)
print(method)
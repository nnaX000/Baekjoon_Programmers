import sys

input=sys.stdin.readline

N,M=map(int,input().split())
edges=[]

for i in range(M):
    edges.append(list(map(int,input().split())))

dist=[float('inf') for _ in range(N+1)]
dist[1]=0
check=False

for i in range(N+1):
    update=False
    for s,e,t in edges:
        if(dist[e]>dist[s]+t):
            update=True
            dist[e]=dist[s]+t

            if(i==N):
                check=True
                break

    if(not update):
        break

if(check):
    print(-1)
else:
    for i in range(2,N+1):
        if(dist[i]!=float('inf')):
            print(dist[i])
        else:
            print(-1)
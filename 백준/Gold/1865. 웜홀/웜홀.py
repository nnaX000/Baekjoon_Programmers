import sys

input=sys.stdin.readline

TC=int(input())

for i in range(TC):
    N,M,W=map(int,input().split())

    edges=[]

    for j in range(M):
        S,E,T=map(int,input().split())
        edges.append([S,E,T])
        edges.append([E,S,T])

    for j in range(W):
        S,E,T=map(int,input().split())
        edges.append([S,E,-T])

    dist=[0 for _ in range(N+1)]

    for i in range(N+1):
        check=False
        update=False

        for s,e,t in edges:
            if(dist[e]>dist[s]+t):
                dist[e]=dist[s]+t
                update=True
                
                if(i==N):
                    check=True
                    break

        if(not update):
            break

    if(not check):
        print("NO")
    else:
        print("YES")
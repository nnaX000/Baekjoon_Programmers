import sys
import heapq

N, M, X = map(int,sys.stdin.readline().split(' '))

max_value=0

road=[[] for i in range(N+1)]

for i in range(M):
    start,end,cost=map(int,sys.stdin.readline().split(' '))
    road[start].append([end,cost])

def dig(a,b,distance):
    q=[]
    heapq.heappush(q,(a,b))

    distance[b]=0

    while(q):
        cost, start = heapq.heappop(q)
        visited[start]=True

        for i in range(len(road[start])):
            if(distance[road[start][i][0]]>distance[start]+road[start][i][1] and not visited[road[start][i][0]]):

                distance[road[start][i][0]]=distance[start]+road[start][i][1]

                heapq.heappush(q,(distance[start]+road[start][i][1], road[start][i][0]))

    return distance

for i in range(1,N+1):
    summ=0

    distance=[float('inf')]*(N+1)
    visited=[False]*(N+1)
    result=dig(0,i,distance)
    summ+=result[X]

    distance=[float('inf')]*(N+1)
    visited=[False]*(N+1)
    result=dig(0,X,distance)
    summ+=result[i]

    if(summ>max_value):
        max_value=summ

print(max_value)
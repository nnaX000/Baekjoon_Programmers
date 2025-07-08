import sys
import heapq

N,E=map(int,sys.stdin.readline().strip().split(' '))

edge=[[] for i in range(N+1)]

for i in range(E):
    start,end,cost=map(int,sys.stdin.readline().strip().split(' '))

    edge[start].append([end,cost])
    edge[end].append([start,cost])

v1,v2=map(int,sys.stdin.readline().strip().split(' '))

def dig(k):
    q=[]
    visited=[False]*(N+1)
    distance=[float('inf')]*(N+1)
    visited[k]=True
    distance[k]=0
    heapq.heappush(q,(0,k))

    while(q):
        cost,start=heapq.heappop(q)
        visited[start]=True

        for i in range(len(edge[start])):
            if(distance[edge[start][i][0]]>distance[start]+edge[start][i][1] and not visited[edge[start][i][0]]):
                distance[edge[start][i][0]]=distance[start]+edge[start][i][1]
                heapq.heappush(q,(distance[start]+edge[start][i][1],edge[start][i][0]))

    return distance


one = dig(1)
v1_path = dig(v1)
v2_path = dig(v2)

path1 = one[v1] + v1_path[v2] + v2_path[N]
path2 = one[v2] + v2_path[v1] + v1_path[N]

result = min(path1, path2)

print(result if result < float('inf') else -1)
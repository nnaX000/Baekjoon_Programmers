import sys
import heapq

V,E=map(int,sys.stdin.readline().rstrip().split(' '))

K=int(sys.stdin.readline().rstrip())

heap=[]

heapq.heappush(heap,[0,K]) #[지금까지 계산한 최단거리,현재인덱스 위치]

short_dis=["INF" for i in range(V+1)]

graph=[[] for i in range(V+1)]

visited=[False for i in range(V+1)]

for i in range(E):
    start,end,weight=map(int,sys.stdin.readline().rstrip().split(' '))
    graph[start].append([end,weight])

while(heap):
    tmp=heapq.heappop(heap)
    current=tmp[1]
    distance=tmp[0]

    if(not visited[current]):
        visited[current]=True
        short_dis[current]=str(distance)

        for i in range(len(graph[current])):
            if(not visited[graph[current][i][0]]):
                heapq.heappush(heap,[distance+graph[current][i][1],graph[current][i][0]])

for i in range(1,len(short_dis)):
    print(short_dis[i])
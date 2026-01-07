import sys
import heapq

input=sys.stdin.readline

V,E=map(int,input().split())
K=int(input())

graph=[[] for _ in range(V+1)]

for i in range(E):
    a,b,cost=map(int,input().split())
    graph[a].append([b,cost])

heap=[]
heapq.heapify(heap)
heapq.heappush(heap,(0,K)) #COST,K

result=[float('inf') for _ in range(V+1)]
result[K]=0

while(heap):
    cost,current=heapq.heappop(heap)

    if(result[current]<cost):
        continue

    for i in range(len(graph[current])):
        if(result[current]+graph[current][i][1]<result[graph[current][i][0]]):
            result[graph[current][i][0]]=result[current]+graph[current][i][1]
            heapq.heappush(heap,(result[current]+graph[current][i][1],graph[current][i][0]))

for i in range(1,V+1):
    if(result[i]==float('inf')):
        print("INF")
    else:
        print(result[i])
import sys
import heapq

input=sys.stdin.readline

V,E=map(int,input().split())
K=int(input())

heap=[]
heapq.heapify(heap)
heapq.heappush(heap,(0,K))
result=[float('inf') for _ in range(V+1)]

node=[[] for _ in range(V+1)]

for i in range(E):
    a,b,c=map(int,input().split())
    node[a].append([b,c])

while(heap):
    cost,current=heapq.heappop(heap)

    if(result[current]<cost):
        continue

    if(cost==0 and current==K):
        result[current]=0

    for i in range(len(node[current])):
        if(result[node[current][i][0]]>cost+node[current][i][1]):
            heapq.heappush(heap,(cost+node[current][i][1],node[current][i][0]))
            result[node[current][i][0]]=cost+node[current][i][1]

for i in range(1,V+1):
    if(result[i]==float('inf')):
        print("INF")
    else:
        print(result[i])
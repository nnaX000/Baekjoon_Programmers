import sys
import heapq

input=sys.stdin.readline

N,M,X=map(int,input().split())

town=[[] for _ in range(N+1)]
town_r=[[] for _ in range(N+1)]

answer=[0 for _ in range(N+1)]

def dij():
    global heap
    global result

    while(heap):
        cost,x=heapq.heappop(heap)

        if(result[x]<cost):
            continue

        if(cost==0 and x==X):
            result[x]=0

        for i in range(len(town[x])):
            if(result[town[x][i][0]]>cost+town[x][i][1]):
                result[town[x][i][0]]=cost+town[x][i][1]
                heapq.heappush(heap,(cost+town[x][i][1],town[x][i][0]))

for i in range(M):
    start,end,T=map(int,input().split())

    town[start].append([end,T])
    town_r[end].append([start,T])

heap=[]
heapq.heapify(heap)
heapq.heappush(heap,(0,X)) # cost, X
result=[float('inf') for _ in range(N+1)]
dij()

for i in range(N+1):
    if(result[i]!=float('inf')):
        answer[i]+=result[i]

heap=[]
heapq.heapify(heap)
heapq.heappush(heap,(0,X))
town=[i[:] for i in town_r]
result=[float('inf') for _ in range(N+1)]
dij()

for i in range(N+1):
    if(result[i]!=float('inf')):
        answer[i]+=result[i]

print(max(answer))
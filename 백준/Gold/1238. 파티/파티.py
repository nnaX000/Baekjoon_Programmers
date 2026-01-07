import sys
import heapq

def dij():
    global result
    global heap

    while(heap):
        cost,current=heapq.heappop(heap)

        if(result[current]<cost):
            continue

        for i in range(len(road[current])):
            if(result[road[current][i][0]]>result[current]+road[current][i][1]):
                result[road[current][i][0]]=result[current]+road[current][i][1]
                heapq.heappush(heap,(result[road[current][i][0]],road[current][i][0]))

input=sys.stdin.readline

N,M,X=map(int,input().split()) # X가 목적지

road=[[] for _ in range(N+1)]
answer=[0 for _ in range(N+1)]

for i in range(M):
    a,b,cost=map(int,input().split())
    road[a].append([b,cost])

for i in range(1,N+1):
    heap=[]
    heapq.heapify(heap)

    heapq.heappush(heap,(0,i)) #cost, 위치
    result=[float('inf') for _ in range(N+1)]
    result[i]=0

    dij()

    if(i==X):
        for i in range(1, N+1):
            answer[i] += result[i]
    else:
        answer[i]+=result[X]

print(max(answer))
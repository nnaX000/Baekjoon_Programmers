import sys
import heapq

#다익스트라

input=sys.stdin.readline

N=int(input())
M=int(input())

bus=[[] for _ in range(N+1)]
heap=[]
answer=[float('inf') for _ in range(N+1)]

heapq.heapify(heap)

for i in range(M):
    a,b,cost=map(int,input().split())
    bus[a].append([b,cost]) # 목적지, 비용

start,end=map(int,input().split())
answer[start]=0

heapq.heappush(heap,(0,start)) # cost, 현재위치

#print(heap)

while(heap):
    cost,pos=heapq.heappop(heap)

    if(answer[pos]<cost):
        continue

    for dt,value in bus[pos]:
        if(answer[dt]>answer[pos]+value):
            answer[dt]=answer[pos]+value
            heapq.heappush(heap,(answer[pos]+value,dt))

print(answer[end])
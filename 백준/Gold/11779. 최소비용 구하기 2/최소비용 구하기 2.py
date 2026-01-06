import sys
import heapq

input=sys.stdin.readline

n=int(input())
m=int(input())

prev=[0 for i in range(n+1)]
answer=[float('inf') for i in range(n+1)]
bus=[[] for i in range(n+1)]
heap=[]
heapq.heapify(heap)

for i in range(m):
    start,end,cost=map(int,input().split())

    bus[start].append([end,cost])

depart,des=map(int,input().split())
heapq.heappush(heap,(0,depart))
answer[depart]=0

while(heap):
    cost,current=heapq.heappop(heap)

    if(answer[current]<cost):
        continue

    for i in range(len(bus[current])):
        if(answer[bus[current][i][0]]>answer[current]+bus[current][i][1]):
            answer[bus[current][i][0]]=answer[current]+bus[current][i][1]
            prev[bus[current][i][0]]=current
            heapq.heappush(heap, (answer[current]+bus[current][i][1],bus[current][i][0]))

tmp=des
route=[]
route.append(tmp)
while(tmp!=0):
    route.append(prev[tmp])
    tmp=prev[tmp]

route=list(reversed(route[:len(route)-1]))

print(answer[des])
print(len(route))
print(*route)
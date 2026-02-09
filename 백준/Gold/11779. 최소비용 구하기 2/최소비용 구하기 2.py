import sys
import heapq

input=sys.stdin.readline

n=int(input()) #도시 개수
m=int(input()) #버스 개수

heap=[]
heapq.heapify(heap)

bus=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,input().split())
    bus[a].append([b,c])

start,end=map(int,input().split())

answer=[float('inf') for _ in range(n+1)]
record=[-1 for _ in range(n+1)]
heapq.heappush(heap,(0,start))

while(heap):
    cost,n=heapq.heappop(heap)

    if(answer[n]<cost):
        continue

    if(cost==0 and n==start):
        answer[n]=0

    for i in range(len(bus[n])):
        if(cost+bus[n][i][1]<answer[bus[n][i][0]]):
            answer[bus[n][i][0]]=cost+bus[n][i][1]
            heapq.heappush(heap,(cost+bus[n][i][1],bus[n][i][0]))
            record[bus[n][i][0]]=n

print(answer[end])
path=[]
path.append(end)
des=end

while(True):
    n=record[des]
    if(n==-1):
        break
    else:
        path.append(n)
        des=n

path.reverse()
print(len(path))
print(*path)
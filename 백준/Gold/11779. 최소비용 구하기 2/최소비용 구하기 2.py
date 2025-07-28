import sys
import heapq

n=int(sys.stdin.readline().rstrip())
m=int(sys.stdin.readline().rstrip())

bus=[[] for i in range(n+1)]

visited=[False for i in range(n+1)]

minimum_cost=[["INF",[]] for i in range(n+1)]

heap=[]

for i in range(m):
    start,end,cost=map(int,sys.stdin.readline().rstrip().split(' '))
    bus[start].append([cost,end])

start_city,finish_city=map(int,sys.stdin.readline().rstrip().split(' '))

heapq.heappush(heap,[0,start_city,[start_city]])#[최단거리, 시작버스, 경로]

while(heap):
    dis,start,path=heapq.heappop(heap)

    if(not visited[start]):
        visited[start]=True
        minimum_cost[start]=[dis,path[:]]
        
        for i in range(len(bus[start])):
            if(not visited[bus[start][i][1]]):
                new_path=path[:]
                new_path.append(bus[start][i][1])
                heapq.heappush(heap,[dis+bus[start][i][0],bus[start][i][1],new_path])

print(minimum_cost[finish_city][0])
print(len(minimum_cost[finish_city][1]))
for i in range(len(minimum_cost[finish_city][1])):
    print(minimum_cost[finish_city][1][i],end=" ")
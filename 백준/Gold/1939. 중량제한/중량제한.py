import sys
import heapq

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
path=[[] for i in range(N+1)]

for i in range(M):
    a,b,cost=map(int,sys.stdin.readline().rstrip().split(' '))
    path[a].append([cost,b])
    path[b].append([cost,a])

f_1,f_2=map(int,sys.stdin.readline().rstrip().split(' '))

visited=[float('-inf') for i in range(N+1)]
visited[f_1]=0

heap=[]
heapq.heapify(heap)
heapq.heappush(heap,(f_1,float('-inf')))

while(heap):
    current, cost = heapq.heappop(heap)
    cost = -cost

    if(visited[current]>cost):
        continue

    if(current==f_2):
        print(cost)
        break

    for i in range(len(path[current])):
        c,d=path[current][i][0],path[current][i][1]
        if(visited[d]<min(c,cost)):
            visited[d]=min(c,cost)
            heapq.heappush(heap,(d,-visited[d]))
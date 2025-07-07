import sys
import heapq

N,M,K,X=map(int,sys.stdin.readline().strip().split(' '))

visited=[False]*(N+1) # 방문한 곳 체크
distance=[float('inf')]*(N+1) # 최단거리 저장하는 곳
city=[[] for i in range(N+1)] #연결정보 저장
answer=[]

q=[]

distance[X]=0

heapq.heappush(q,(0,X))

for i in range(M):
    start,end=map(int,sys.stdin.readline().split(' '))
    city[start].append(end)

while(q):
    dis, stand = heapq.heappop(q)
    visited[stand]=True

    for i in range(len(city[stand])):
        if(distance[city[stand][i]]>distance[stand]+1 and not visited[city[stand][i]]):
            distance[city[stand][i]]=distance[stand]+1

            heapq.heappush(q,(distance[stand]+1, city[stand][i]))

for i in range(1,N+1):
    if(distance[i]==K):
        answer.append(i)

if(len(answer)!=0):
    for i in answer:
        print(i)
else:
    print(-1)
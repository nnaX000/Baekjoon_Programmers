import sys
import heapq

input=sys.stdin.readline
answer=[]

while(True):
    m,n=map(int,input().split())

    if(m==0 and n==0):
        break

    hq=[]
    sum_value=0
    heapq.heapify(hq)
    heapq.heappush(hq,(0,1)) # cost, des

    visited=[False for _ in range(m+1)]

    roads=[[] for _ in range(m)]

    for _ in range(n):
        x,y,z=map(int,input().split())
        sum_value+=z

        roads[x].append([y,z]) # des, cost
        roads[y].append([x,z]) # des, cost

    occupy=0
    occupy_cost=0

    while(hq):
        cost,des=heapq.heappop(hq)

        if(not visited[des]):
            occupy+=1
            visited[des]=True
            occupy_cost+=cost

            if(occupy==m):
                break

            for d,c in roads[des]:
                if(not visited[d]):
                    heapq.heappush(hq,(c,d))

    answer.append(sum_value-occupy_cost)

for i in answer:
    print(i)
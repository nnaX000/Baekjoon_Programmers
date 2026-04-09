import sys
import math
import heapq

input=sys.stdin.readline

n=int(input())
star=[]
hq=[]
heapq.heapify(hq)

position=[[] for _ in range(n)]

def calcul(x1,y1,x2,y2):
    tmp=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return tmp

for _ in range(n):
    x,y=map(float,input().split())
    star.append([x,y])

for i in range(n):
    for j in range(i+1,n):
        x1,y1=star[i][0],star[i][1]
        x2,y2=star[j][0],star[j][1]

        distance=calcul(x1,y1,x2,y2)

        position[i].append([j,distance])
        position[j].append([i,distance])

heapq.heappush(hq,(0,0)) #cost, start
visited=[False for _ in range(n)]
cnt=0

answer=0

while hq:
    cost,des=heapq.heappop(hq)

    if(not visited[des]):
        cnt+=1
        answer+=cost
        visited[des]=True

        if(cnt==n):
            break

        for d,c in position[des]:
            if(not visited[d]):
                heapq.heappush(hq,(c,d))

print(f"{answer:.2f}")
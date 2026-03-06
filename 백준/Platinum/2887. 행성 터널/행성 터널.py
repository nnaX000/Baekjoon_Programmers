import sys
import heapq

input=sys.stdin.readline

# 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)

def find(x):
    if(parent[x]==x):
        return x
    return find(parent[x])

def union(x,y):
    px,py=find(x),find(y)

    if(px==py):
        return False
    elif(rank[px]<rank[py]):
        parent[px]=py
    elif(rank[py]>rank[py]):
        parent[py]=px
    elif(rank[px]==rank[px]):
        parent[py]=px
        rank[px]+=1

    return True

N=int(input()) # 행성 개수
parent=[i for i in range(N)]
rank=[0 for _ in range(N)]

planet=[]
hq=[]
heapq.heapify(hq)

for i in range(N):
    x,y,z=map(int,input().split())
    planet.append([x,y,z,i])

planet.sort(key=lambda x:x[0])

for i in range(N-1):
    tmp=abs(planet[i][0]-planet[i+1][0])
    heapq.heappush(hq,(tmp,planet[i][3],planet[i+1][3]))

planet.sort(key=lambda x:x[1])

for i in range(N-1):
    tmp=abs(planet[i][1]-planet[i+1][1])
    heapq.heappush(hq,(tmp,planet[i][3],planet[i+1][3]))

 
planet.sort(key=lambda x:x[2])

for i in range(N-1):
    tmp=abs(planet[i][2]-planet[i+1][2])
    heapq.heappush(hq,(tmp,planet[i][3],planet[i+1][3]))

count=0
answer=0

while(hq):
    cost,start,end=heapq.heappop(hq)

    if union(start,end):
        count+=1
        answer+=cost

        if(count==N-1):
            print(answer)
            break
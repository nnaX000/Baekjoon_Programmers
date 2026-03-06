import sys
import heapq

input=sys.stdin.readline

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
    elif(rank[px]>rank[py]):
        parent[py]=px
    elif(rank[px]==rank[py]):
        parent[py]=px
        rank[px]+=1
    return True

hq=[]
heapq.heapify(hq)

V,E=map(int,input().split())
edges=[[] for _ in range(V+1)]
parent=[i for i in range(V+1)]
rank=[0 for _ in range(V+1)]

count=0
answer=0

for i in range(E):
    a,b,c=map(int,input().split())

    heapq.heappush(hq,(c,a,b))

while(hq):
    cost,start,end=heapq.heappop(hq)

    if union(start,end):
        count+=1
        answer+=cost

        if(count==V-1):
            print(answer)
            break
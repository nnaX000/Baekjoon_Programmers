import sys

input=sys.stdin.readline

answer=0
answer_t=[]

def find(x):
    if(parents[x]==x):
        return x
    return find(parents[x])

def union(x,y):
    px,py=find(x),find(y)

    if(px==py):
        return False
    elif(rank[px]<rank[py]):
        parents[px]=py
    elif(rank[px]>rank[py]):
        parents[py]=px
    elif(rank[px]==rank[py]):
        parents[py]=px
        rank[px]+=1

    return True

n,m=map(int,input().split())

parents=[i for i in range(n+1)]
rank=[0 for _ in range(n+1)]

count=0

for i in range(m):
    x,y=map(int,input().split())

    if union(x,y):
        count+=1

edges=[]

for i in range(n):
    tmp=list(map(int,input().split()))
    if(i!=0):
        for j in range(len(tmp)):
            if(j!=0):
                edges.append([tmp[j],i+1,j+1])

edges.sort(key=lambda x:x[0])

for cost,start,end in edges:
    if union(start,end):
        count+=1
        answer+=cost
        answer_t.append([start,end])

        if(count==n-2):
            break

print(answer,len(answer_t))
for i in answer_t:
    print(*i)
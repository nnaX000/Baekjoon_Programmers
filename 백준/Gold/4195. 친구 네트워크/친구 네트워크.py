import sys
from collections import defaultdict

input=sys.stdin.readline

T=int(input())

def find(x):
    if(parent[x]==x):
        return x
    
    return find(parent[x])

def union(x,y):
    px,py=find(x),find(y)

    if(px==py):
        return True
    else:
        if(rank[px]<rank[py]):
            parent[px]=py
            friends[py]+=friends[px]
            friends[px]=0
        elif(rank[px]>rank[py]):
            parent[py]=px
            friends[px]+=friends[py]
            friends[py]=0
        else:
            rank[px]+=1
            parent[py]=px
            friends[px]+=friends[py]
            friends[py]=0

    return False

for i in range(T):
    F=int(input())
    rel=[]

    parent=defaultdict(str)
    rank=defaultdict(int)
    friends=defaultdict(int)
    answer=[]

    for j in range(F):
        a,b=input().rstrip().split()
        rel.append([a,b])

        parent[a]=a
        parent[b]=b

        rank[a]=0
        rank[b]=0

        friends[a]=1
        friends[b]=1

    for a,b in rel:
        union(a,b)
        #print(parent)
        #print(friends)
        answer.append(friends[find(a)])

    for i in answer:
        print(i)
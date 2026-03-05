import sys

input=sys.stdin.readline

N=int(input())
M=int(input())

parent=[i for i in range(N+1)]
rank=[0 for _ in range(N+1)]

def find(x):
    if(parent[x]==x):
        return x
    return find(parent[x])

def union(x,y):
    px,py=find(x),find(y)

    if(px==py):
        return
    elif(rank[px]<rank[py]):
        parent[px]=py
    elif(rank[py]<rank[px]):
        parent[py]=px
    else:
        parent[py]=px
        rank[px]+=1

for i in range(N):
    tmp=list(map(int,input().split()))

    for j in range(len(tmp)):
        if(tmp[j]==1):
            union(i+1,j+1)

plan=list(set(list(map(int,input().split()))))
stand=find(plan[0])
check=False

for i in range(1,len(plan)):
    if(stand!=find(plan[i])):
        check=True
        break

if(not check):
    print("YES")
else:
    print("NO")
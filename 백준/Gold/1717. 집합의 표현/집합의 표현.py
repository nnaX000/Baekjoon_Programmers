import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**6)

n,m=map(int,input().split())

parent=[i for i in range(n+1)]
rank=[0]*(n+1)
answer=[]

def find(x):
    if(parent[x]==x):
        return x
    return find(parent[x])

def union(x,y):
    pa,pb=find(x),find(y)

    if(pa==pb):
        return
    elif(rank[pa]<rank[pb]):
        parent[pa]=pb
    elif(rank[pa]>rank[pb]):
        parent[pb]=pa
    else:
        rank[pa]+=1
        parent[pb]=pa

for i in range(m):
    command,a,b=map(int,input().split())

    if(command==0):
        union(a,b)
    else:
        answer.append("YES" if find(a)==find(b) else "NO")

for i in answer:
    print(i)
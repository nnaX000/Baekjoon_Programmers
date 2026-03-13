import sys

input=sys.stdin.readline

def find(x):
    global parent

    if(parent[x]==x):
        return x
    
    return find(parent[x])

def union(x,y):
    global rank
    global parent
    global cycle

    px,py=find(x),find(y)

    if(px in cycle):
        cycle.add(py)

    if(py in cycle):
        cycle.add(px)

    if(px==py):
        return True
    else:
        if(rank[px]<rank[py]):
            parent[px]=py
        elif(rank[px]>rank[py]):
            parent[py]=px
        else:
            rank[px]+=1
            parent[py]=px
    return False

answer=[]

while(True):
    n,m=map(int,input().split()) #노드 수, 간선 수

    if(n==0 and m==0):
        break

    parent=[i for i in range(n+1)]
    rank=[0 for _ in range(n+1)]
    equals=[]
    cycle=set()

    for i in range(m):
        a,b=map(int,input().split())
        if (a==b):
            equals.append(a)
        if union(a,b):
            cycle.add(find(a))

    for i in equals:
        cycle.add(find(parent[i]))

    unique=set()
    for i in range(1, len(parent)):
        root = find(i)
        if root not in cycle:
            unique.add(root)

    answer.append(len(unique))

for i in range(len(answer)):
    if(answer[i]==0):
        print("Case "+str(i+1)+": "+"No trees.")
    elif(answer[i]==1):
        print("Case "+str(i+1)+": "+"There is one tree.")
    else:
        print("Case " +str(i+1)+": "+"A forest of "+str(answer[i])+" trees.")
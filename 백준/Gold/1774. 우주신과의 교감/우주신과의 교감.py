import sys

input=sys.stdin.readline

answer=0

def find(x):
    if(parent[x]!=x):
        return find(parent[x])
    
    return parent[x]

def union(x,y):
    px,py=find(x),find(y)

    if(px==py):
        return False
    elif(rank[px]<rank[py]):
        parent[px]=py
    elif(rank[py]<rank[px]):
        parent[py]=px
    elif(rank[px]==rank[py]):
        parent[py]=px
        rank[px]+=1
    return True

N,M=map(int,input().split())
parent=[i for i in range(N+1)]
rank=[0 for _ in range(N+1)]

# 통로들의 길이는 2차원 좌표계상의 거리
distance=[]

tmp=[list(map(int,input().split())) for _ in range(N)]

for i in range(N-1):
    for j in range(i+1,N):
        dx = tmp[i][0] - tmp[j][0]
        dy = tmp[i][1] - tmp[j][1]
        result = (dx*dx + dy*dy) ** 0.5

        distance.append([result,i+1,j+1])

distance.sort(key=lambda x:x[0])

pick=0

for i in range(M):
    x,y=map(int,input().split())
    if union(x,y):  
        pick+=1

for cost,start,end in distance:
    if (union(start,end)):
        answer+=cost
        pick+=1

        if(pick==N-1):
            break

print(f"{answer:.2f}")
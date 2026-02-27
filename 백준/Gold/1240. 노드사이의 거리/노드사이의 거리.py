import sys
import heapq

input=sys.stdin.readline

N,M=map(int,input().split())

hq=[]
heapq.heapify(hq)

answer=[[float('inf') for _ in range(N+1)] for _ in range(N+1)]
tree=[[] for _ in range(N+1)]

for i in range(N-1):
    a,b,c=map(int,input().split())

    tree[a].append([b,c])
    tree[b].append([a,c])

for i in range(M):
    a,b=map(int,input().split())
    
    hq=[]
    heapq.heapify(hq)
    heapq.heappush(hq,(0,a))

    if(answer[a][b]!=float('inf')):
        print(answer[a][b])
    else:
        while(hq):
            cost,pos=heapq.heappop(hq)

            if(answer[a][pos]<cost):
                continue

            if(pos==a):
                answer[a][a]=0

            for i in range(len(tree[pos])):
                if(answer[a][tree[pos][i][0]]>cost+tree[pos][i][1]):
                    answer[a][tree[pos][i][0]]=cost+tree[pos][i][1]
                    heapq.heappush(hq,(cost+tree[pos][i][1],tree[pos][i][0]))

        print(answer[a][b])
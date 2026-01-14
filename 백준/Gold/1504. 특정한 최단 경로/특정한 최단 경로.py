import sys
import heapq

#다익스트라 분해 문제

#구해야 하는 것
#1->V1 , 1->V2 : 1
#V1->V2 , V1->N : V1
#V2->N :V2

input=sys.stdin.readline

answer=[0,0]

N,E=map(int,input().split())
graph=[[] for _ in range(N+1)]

for i in range(E):
    a,b,c=map(int,input().split())

    graph[a].append([b,c]) # 노드, cost
    graph[b].append([a,c]) # 노드, cost

V1,V2=map(int,input().split())

def djk(current):
    heap=[]
    heapq.heappush(heap,(0,current))
    result=[float('inf') for _ in range(N+1)]
    result[current]=0

    while(heap):
        cost,now=heapq.heappop(heap)

        if(result[now]<cost):
            continue
        
        for j in range(len(graph[now])):
            if(result[graph[now][j][0]]>result[now]+graph[now][j][1]):
                result[graph[now][j][0]]=result[now]+graph[now][j][1]
                heapq.heappush(heap,(result[now]+graph[now][j][1],graph[now][j][0]))


    return result

dv=djk(1)
dv_1=djk(V1)
dv_2=djk(V2)

answer_1=dv[V1]+dv_1[V2]+dv_2[N]
answer_2=dv[V2]+dv_2[V1]+dv_1[N]

if(answer_1==float('inf') or answer_2==float('inf')):
    print(-1)
else:
    print(min(answer_1,answer_2))
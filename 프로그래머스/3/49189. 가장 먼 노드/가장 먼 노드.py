import heapq

def solution(n, edge):
    answer = 0
    vertex=[[] for i in range(n+1)]
    min_dist=[0 for i in range(n+1)]
    visited=[False for i in range(n+1)]
    heap=[]
    heapq.heapify(heap)
    
    for a,b in edge : 
        vertex[a].append(b)
        vertex[b].append(a)
        
    heapq.heappush(heap,(0,1)) # 거리, 노드
    
    while(heap):
        dist,node=heapq.heappop(heap)
        if(not visited[node]):
            min_dist[node]=dist
            visited[node]=True

            for i in vertex[node]:
                if(not visited[i]):
                    heapq.heappush(heap,(dist+1,i))
    
    
    max_value=max(min_dist)

    for i in range(1,n+1):
        if(min_dist[i]==max_value):
            answer+=1
            
    return answer
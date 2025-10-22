import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for i in range(N+1)]
    heap = []
    visited=set()
    
    for i in range(len(road)):
        start, end, cost = road[i]
        graph[start].append([end,cost])
        graph[end].append([start,cost])
    
    heapq.heapify(heap)
    heapq.heappush(heap,(0,1))#cost, node위치
    
    while(heap):
        cost, node = heapq.heappop(heap)
        
        if(node not in visited):
            visited.add(node)
            
            if(cost<=K):
                answer+=1
                
            for i in range(len(graph[node])):
                heapq.heappush(heap,(cost+graph[node][i][1],graph[node][i][0]))
                
    return answer
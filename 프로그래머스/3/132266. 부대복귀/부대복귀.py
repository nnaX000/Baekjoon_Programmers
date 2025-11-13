import heapq

def solution(n, roads, sources, destination):
    answer = []
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap,(0,destination))
    
    min_length = [float('inf') for i in range(n+1)]
    min_length[destination] = 0
    road = [[] for i in range(n+1)]
    visited = set()
    visited.add(destination)
    
    for x,y in roads:
        road[x].append(y)
        road[y].append(x)
    
    while(heap):
        cost, des = heapq.heappop(heap)
        visited.add(des)
        min_length[des] = cost
        
        if cost > min_length[des]:
            continue
        
        for i in range(len(road[des])):
            if(min_length[road[des][i]] > cost+1):
                min_length[road[des][i]] = cost+1
                heapq.heappush(heap,(cost+1,road[des][i]))
                
    for i in sources:
        if(min_length[i]==float('inf')):
            answer.append(-1)
        else:
            answer.append(min_length[i])
        
    return answer
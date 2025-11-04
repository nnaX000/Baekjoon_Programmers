import heapq

def solution(n, k, enemy):
    heap=[]
    heapq.heapify(heap)
    
    for i in range(len(enemy)):
        heapq.heappush(heap,enemy[i])
        
        if(len(heap)>k):
            n-=heapq.heappop(heap)
        if(n<0):
            return i
        
    return len(enemy)
    
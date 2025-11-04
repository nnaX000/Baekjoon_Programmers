import heapq
def solution(scores):
    answer = -1
    heap = []
    sum_value = []
    heapq.heapify(heap)
    stand = float('-inf')
    wanho_id = scores[0]
    wanho = sum(scores[0])
    candi = set()
    
    for a,b in scores:
        heapq.heappush(heap,[-1*a,b])
    
    while(heap):
        attitude, coworker = heapq.heappop(heap)
        attitude = -1*attitude
        
        if(coworker>=stand):
            stand = coworker
            sum_value.append(attitude+coworker)
            candi.add((attitude,coworker))
    
    if(tuple(wanho_id) in candi):
        sum_value.sort(reverse=True)

        for idx,i in enumerate(sum_value):
            if(i==wanho):
                answer=idx+1
                break

        return answer 
    else:
        return -1
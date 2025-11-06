import heapq

def solution(A, B):
    answer = 0
    A.sort()

    heapq.heapify(B)
    tmp=heapq.heappop(B)
    
    for i in range(len(A)):
        while(tmp<=A[i]):
            if(B):
                tmp = heapq.heappop(B)
            else:
                return answer
            
        answer+=1
        if(B):
            tmp = heapq.heappop(B)
        else:
            return answer
        
    return answer
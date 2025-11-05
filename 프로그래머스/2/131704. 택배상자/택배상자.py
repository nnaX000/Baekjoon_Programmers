from collections import deque

def solution(order):
    answer = 0
    dequee = deque()
    stand = 1
    stand_nxt = 1
    
    for i in range(len(order)):
        if(order[i]>=stand):
            for j in range(stand_nxt,order[i]):
                dequee.append(j)
            
            answer+=1
            stand=order[i]
            
            if(i<len(order)-1):
                stand_nxt=order[i]+1
            
        else:
            if(dequee):
                tmp = dequee.pop()

                if(tmp != order[i]):
                    return answer
                else:
                    answer+=1
                
    return answer
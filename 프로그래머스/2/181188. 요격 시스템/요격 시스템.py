def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    position=0
    
    for i in range(len(targets)):
        if(not (targets[i][0]<position<targets[i][1])):
            answer+=1
            position=targets[i][1]-0.1
            
    return answer
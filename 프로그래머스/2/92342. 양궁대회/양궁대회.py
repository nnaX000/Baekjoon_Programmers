from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_sub = float('-inf')
    
    for i in combinations_with_replacement([0,1,2,3,4,5,6,7,8,9,10],n):
        ryan = [0 for i in range(11)]
        
        ryan_score=0
        peach_score=0
        
        for j in i:
            ryan[(10-j)]+=1
        
        for idx,i in enumerate(ryan):
            if(ryan[idx]>0 or info[idx]>0):
                if(i<=info[idx]):
                    peach_score+=(10-idx)
                else:
                    ryan_score+=(10-idx)
                    
        if(peach_score<ryan_score and (ryan_score-peach_score)>max_sub):
            max_sub = ryan_score-peach_score
            answer = ryan[:]
            
    return answer
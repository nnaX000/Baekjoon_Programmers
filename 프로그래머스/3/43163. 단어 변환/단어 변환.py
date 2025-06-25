from collections import deque

def solution(begin, target, words):
    answer=0
    set_words=set(words)
    dequee=deque(begin)
    dequee=deque([[begin,answer]])
    stop=False
    
    if(target not in set_words):
        return 0
    
    while(dequee):
        word,answer=dequee.popleft()
        
        for i in words:
            count=0
            for jdx,j in enumerate(i):
                if(j!=word[jdx]):
                    count+=1

            if(count==1):
                if(i==target):
                    stop=True
                    break
                else:
                    dequee.append([i,answer+1])
        
        if(stop):
            answer+=1
            break
            
    return answer
            
    

                
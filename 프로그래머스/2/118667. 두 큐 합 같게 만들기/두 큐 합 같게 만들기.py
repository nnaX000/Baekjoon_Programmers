from collections import deque

def solution(queue1, queue2):
    dequee_1 = deque(queue1)
    dequee_2 = deque(queue2)
    
    s1 = sum(dequee_1)
    s2 = sum(dequee_2)
    
    max_depth = 5*(max(len(queue1),len(queue2)))
    check=False
    sum_value = sum(dequee_1)+sum(dequee_2)
    target = sum_value // 2

    answer = 0
    
    if(sum_value%2==-1):
        return -1
    
    while (answer<=max_depth):
        
        if(s1>target):
            while (s1 > target):
                tmp = dequee_1.popleft()
                s1-=tmp
                dequee_2.append(tmp)
                s2+=tmp
                answer+=1
                
        elif(s1<target):
            while (s1 < target):
                tmp = dequee_2.popleft()
                s2-=tmp
                dequee_1.append(tmp)
                s1+=tmp
                answer+=1
        
        if(s1==target):
            check=True
            break

    return answer if check else -1
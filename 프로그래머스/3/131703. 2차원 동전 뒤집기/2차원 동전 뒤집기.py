from collections import deque

def solution(beginning, target):
    answer = 10000
    n, m = len(beginning), len(beginning[0])
    
    for i in range(1<<n):
        count = 0
        tmp = [j[:] for j in beginning]
        
        for j in range(n):
            if i & (1 << j):
                count += 1
                for k in range(m):
                    tmp[j][k]^=1
                    
        for j in range(m):
            if any(tmp[k][j]!=target[k][j] for k in range(n)):
                count+=1
                for k in range(n):
                    tmp[k][j]^=1
                    
        if(tmp==target):
            answer=min(answer,count)
    
    return answer if answer!=10000 else -1
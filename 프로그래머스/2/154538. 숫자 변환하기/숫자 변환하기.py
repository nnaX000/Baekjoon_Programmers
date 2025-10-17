from collections import deque
def solution(x, y, n):
    answer = 0
    visited = set()
    dequee = deque()
    dequee.append((x,0)) # 숫자, count
    
    while(dequee):
        tmp,count = dequee.popleft()
        
        if(tmp==y):
            return count
        
        if(tmp+n not in visited and tmp+n<=y):
            visited.add(tmp+n)
            dequee.append((tmp+n,count+1))
        
        if(tmp*2 not in visited and tmp*2<=y):
            visited.add(tmp*2)
            dequee.append((tmp*2,count+1))
            
        if(tmp*3 not in visited and tmp*3<=y):
            visited.add(tmp*3)
            dequee.append((tmp*3,count+1))
            
    return -1
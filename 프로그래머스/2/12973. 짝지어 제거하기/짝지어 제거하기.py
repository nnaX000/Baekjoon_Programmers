from collections import deque

def solution(s):
    
    dequee=deque()
    
    for i in s:
        if(dequee and dequee[-1]==i):
            dequee.pop()
        else:
            dequee.append(i)
        
    return 1 if not dequee else 0
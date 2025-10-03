from collections import deque, defaultdict

def solution(msg):
    answer=[]
    alpha = defaultdict(int)
    mes = list(msg)
    dequee = deque(mes)
    num = 1
    
    for i in range(65,91):
        alpha[chr(i)] = num
        num+=1
    
    while(dequee):
        tmp = dequee.popleft()
        
        while(tmp in alpha and dequee):
            tmp+=dequee.popleft()
        
        if(tmp not in alpha):
            alpha[tmp] = num
            num+=1
            dequee.appendleft(tmp[-1])
            tmp=tmp[0:len(tmp)-1]
            answer.append(alpha[tmp])
        else:
            answer.append(alpha[tmp])
        
    return answer
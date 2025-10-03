from itertools import permutations
from collections import deque

def solution(expression):
    split_ex=[]
    tmp=""
    for i in range(len(expression)):
        if(expression[i]=="+" or expression[i]=="-" or expression[i]=="*"):
            split_ex.append(int(tmp))
            split_ex.append(expression[i])
            tmp=""
        else:
            tmp+=expression[i]

    split_ex.append(int(tmp))

    answer = float('-inf')
    buho = set()
    
    for i in range(1,len(split_ex),2):
        buho.add(split_ex[i])
        
    buho = list(buho)
    
    for i in permutations(buho,len(buho)):
        dequee = deque(split_ex)
        for j in i:
            length = len(dequee)
            count = 0
            while(count < length):
                tmp = dequee.popleft()
                count+=1
                
                if(tmp == j):
                    tmp_2 = int(dequee.popleft())
                    count+=1
                    if(j == "*"):
                        dequee.append(int(dequee.pop())*tmp_2)
                    elif(j == "+"):
                        dequee.append(int(dequee.pop())+tmp_2)
                    else:
                        dequee.append(int(dequee.pop())-tmp_2)
                else:
                    dequee.append(tmp)

        if(dequee):
            result = abs(dequee.pop())
            if result>answer:
                answer=result
            
    return answer
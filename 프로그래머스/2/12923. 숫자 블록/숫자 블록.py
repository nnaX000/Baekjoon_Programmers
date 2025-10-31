import math
def solution(begin, end):
    answer=[]
    
    for i in range(begin,end+1):
        if(i==1):
            answer.append(0)
            continue
            
        max_value=1
        
        for j in range(2,int(math.sqrt(i))+1): #몫 기준
            if(i%j==0):
                partner = i//j
                if(partner <= 10**7):
                    max_value = max(max_value,partner)
                    break
                else:
                    max_value = max(max_value,j)

        answer.append(max_value)
                
    return answer
from math import sqrt,floor,ceil

def solution(r1, r2):
    answer = 0

    for i in range(1,r2):
        if((r1**2)-(i**2)<0):
            one = 0
        else:
            one = sqrt((r1**2)-(i**2))
            
        two = sqrt((r2**2)-(i**2))
        
        answer += floor(two) - ceil(one) + 1
        
        if(i==r1):
            answer-=1
    
    answer*=4
    answer+=8
    
    return answer
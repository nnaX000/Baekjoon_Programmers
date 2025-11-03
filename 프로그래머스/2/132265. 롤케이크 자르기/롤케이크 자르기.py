from collections import Counter
def solution(topping):
    answer = 0
    num = Counter(topping)
    chulsu = set()
    for i in topping:
        chulsu.add(i)
        num[i]-=1
        
        if(num[i]==0):
            del num[i]
            
        if(len(chulsu) == len(num)):
            answer+=1
    return answer
from itertools import product, combinations
from collections import Counter

def solution(dice):
    num = len(dice)//2
    answer = []
    candi = []
    max_value = float('-inf')
    
    for i in range(num*2):
        candi.append(i)
    
    for i in combinations(candi,num):
        array = []
        rival_array = []
        rival = []
        ac = Counter()
        bc = Counter()
        max_b=0
        win = 0 

        for j in range(num*2):
            if(j not in i):
                rival.append(j)

        for j in range(len(i)):
            array.append(dice[i[j]])

        for j in range(len(rival)):
            rival_array.append(dice[rival[j]])

        for j in product(*array):
            ac[sum(j)]+=1
            
        for j in product(*rival_array):
            tmp=sum(j)
            bc[tmp]+=1
            if(tmp>max_b):
                max_b = tmp
        
        b_prefix = [0 for j in range(max_b+1)]
        
        for key,value in bc.items():
            b_prefix[key] += value
            
        for j in range(1,max_b+1):
            b_prefix[j]+=b_prefix[j-1]

        for key,value in ac.items():
            if(key-1<max_b):
                win+=value*(b_prefix[key-1])
            else:
                win+=value*(b_prefix[-1])
                
            if(win>max_value):
                max_value = win
                answer = i
    
    answer=list(answer)
    
    for i in range(len(answer)):
        answer[i]+=1
    
    return answer
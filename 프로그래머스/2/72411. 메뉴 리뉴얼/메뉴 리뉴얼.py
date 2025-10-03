from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    menu = defaultdict(int)
    for i in orders:
        tmp=list(i)
        for j in range(2,len(i)+1):
            for k in combinations(tmp,j):
                n_k=list(k)
                n_k.sort()
                n_k=tuple(n_k)
                menu_tmp = ''.join(n_k)
                menu[menu_tmp]+=1
    
    max_length = []
    
    for idx,i in enumerate(course):
        max_value = 0
        for key,value in menu.items():
            if(len(key) == i and value>max_value):
                max_value=value
        if(max_value>1):
            max_length.append(max_value)
        else:
            max_length.append(0)
    
    for idx,i in enumerate(max_length):
        for key,value in menu.items():
            if(len(key) == course[idx] and value==i):
                answer.append(key)
    
    answer.sort()
    
    return answer
from itertools import permutations
from collections import Counter

def solution(weights):
    answer = 0
    weight = Counter(weights)
    
    combi = [[1,1],[3,2],[2,1],[4,3]] #[(1, 1), (2, 3), (1, 2), (3, 4)]
    
    for key,value in weight.items():
        for a,b in combi:
            if(key%a!=0):
                continue
            stand=key//a
            if(stand*b in weight):
                if(stand*b == key):
                    answer += weight[key] * (weight[key] - 1) // 2
                else:
                    answer+=weight[stand*b]*value
                
    return answer
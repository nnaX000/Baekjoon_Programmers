from itertools import product

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    candi = []
    
    for i in range(1,6):
        for j in product(alpha,repeat=i):
            candi.append(str(''.join(j)))
    
    candi.sort()
    
    return candi.index(word)+1
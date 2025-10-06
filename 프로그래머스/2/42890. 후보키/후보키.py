from itertools import combinations

def solution(relation):
    answer = set()
    candi = [i for i in range(len(relation[0]))]
    column = len(relation[0])
    
    for i in range(1,column+1):
        for j in combinations(candi,i):
            check = False
            pool = set()
            for k in range(len(relation)):
                tmp = []
                for l in j:
                    tmp.append(relation[k][l])
                
                if(tuple(tmp) not in pool):
                    pool.add(tuple(tmp))
                else:
                    check = True
                    break
                    
            if(not check):
                if(len(j)>1):
                    final = False
                    for n in range(1,len(j)):
                        for o in combinations(j,n):
                            if(o in answer):
                                final=True
                                break
                        if(final):
                            break
                    if(not final):
                        answer.add(j)
                else:
                     answer.add(j)
                        
    return len(answer)
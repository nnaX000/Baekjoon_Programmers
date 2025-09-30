from itertools import permutations

def solution(numbers):
    answer = 0
    piece = list(numbers)
    visited = set()
    
    for i in range(1,len(numbers)+1):
        for j in permutations(piece,i):
            
            tmp = int(''.join(j))
            check=True
            
            if(tmp not in visited and tmp!=0 and tmp!=1):
                for k in range(2,int(tmp**1/2)+1):
                    if(tmp%k==0):
                        check=False
                        break

                if(check):
                    print(tmp)
                    answer+=1
                    visited.add(tmp)
                
    return answer
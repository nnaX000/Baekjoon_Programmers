import math

def solution(n, k):
    answer = []
    person = []
    k-=1
    
    nums = [i for i in range(1,n+1)]
    
    for i in range(n,0,-1):
        result = math.factorial(i-1) 
        idx = k//result
        answer.append(nums.pop(idx))
        k%=result #해당 블록안에서 몇번째에 해당하는지 볼 수 있음
        
    return answer
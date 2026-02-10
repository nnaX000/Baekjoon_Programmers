from functools import cmp_to_key

def solution(numbers):
    s_n=list(map(str,numbers))
    
    s_n.sort(key = lambda x: x*3, reverse = True)
    answer=''.join(s_n)
    
    return answer if int(answer)!=0 else '0'

from functools import cmp_to_key

def solution(numbers):
    s_n=list(map(str,numbers))
    
    def compare(a,b):
        if(int(a+b)>int(b+a)):
            return -1
        elif(int(a+b)<int(b+a)):
            return 1
        return 0
    
    s_n.sort(key=cmp_to_key(compare))
    
    answer=''.join(s_n)
    
    return answer if int(answer)!=0 else "0"

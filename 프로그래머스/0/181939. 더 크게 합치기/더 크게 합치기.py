def solution(a, b):
    answer = 0
    tmp_1=int(str(a)+str(b))
    tmp_2=int(str(b)+str(a))
    
    if(tmp_1>tmp_2):
        return tmp_1
    else:
        return tmp_2
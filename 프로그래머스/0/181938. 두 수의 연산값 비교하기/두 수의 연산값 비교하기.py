def solution(a, b):
    answer = 0
    tmp=int(str(a)+str(b))
    tmp_2=2*a*b
    if(tmp>tmp_2):
        return tmp
    else:
        return tmp_2
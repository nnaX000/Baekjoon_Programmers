def solution(n, lost, reserve):
    reserve=sorted(reserve)
    lost=sorted(lost)
    new_reserve=reserve.copy()
    for j in new_reserve :
        if(j in lost):
            lost.remove(j)
            reserve.remove(j)
    for i in reserve : 
        if(i-1 in lost):
            lost.remove(i-1)
        elif(i+1 in lost):
            lost.remove(i+1)
    return n-len(lost)
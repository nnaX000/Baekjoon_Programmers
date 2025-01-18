from itertools import combinations, permutations

def solution(clothes):
    tmp=1
    answer = 0
    print(answer)
    closet={}
    for i in clothes:
        if(i[1] in closet):
            closet[i[1]]+=1
        else:
            closet[i[1]]=1
    tmp=1
    for i in closet.values():
        tmp*=i+1
    return answer+tmp-1
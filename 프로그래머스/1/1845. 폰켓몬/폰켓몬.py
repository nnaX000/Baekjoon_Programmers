def solution(nums):
    answer = 0
    can_get=len(nums)/2
    unique_keys=0
    dic={}
    for i in nums:
        if (i in dic):
            dic[i]+=1
        else:
            dic[i]=1
            unique_keys+=1
    if(unique_keys<=can_get):
        answer=unique_keys
    else:
        answer=can_get
    return answer
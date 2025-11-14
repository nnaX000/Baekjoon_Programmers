def solution(num_list):
    answer = -100
    for idx,i in enumerate(num_list):
        if(i<0):
            answer = idx
            break
    return answer if answer!=-100 else -1
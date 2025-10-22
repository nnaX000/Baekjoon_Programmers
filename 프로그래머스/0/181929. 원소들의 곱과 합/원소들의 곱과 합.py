def solution(num_list):
    answer = 0
    sum_value = 0
    multi_value = 1
    
    for i in num_list:
        sum_value += i
        multi_value *= i
        
    if((sum_value)**2>multi_value):
        answer = 1
    else:
        answer = 0
        
    return answer
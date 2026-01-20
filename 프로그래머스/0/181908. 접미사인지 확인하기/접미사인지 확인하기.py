def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)):
        tmp=my_string[i:len(my_string)]
        if(is_suffix == tmp):
            answer=1
            break
    return answer
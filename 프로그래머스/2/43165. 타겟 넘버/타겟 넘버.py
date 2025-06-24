def solution(numbers, target):
    answer=0
    
    def dfs(number_count, sum_value):
        nonlocal answer
        if(number_count==len(numbers)):
            if(sum_value==target):
                answer+=1
                return
        else:
            minus_sum_value=sum_value+(-1)*numbers[number_count]
            minus_count=number_count+1
            dfs(minus_count,minus_sum_value)
        
            plus_sum_value=sum_value+numbers[number_count]
            plus_count=number_count+1
            dfs(plus_count,plus_sum_value)
        
    dfs(0,0)
    
    return answer
        
            
                
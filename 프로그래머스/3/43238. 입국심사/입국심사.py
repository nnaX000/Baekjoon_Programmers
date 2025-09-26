def solution(n, times):
    start=1
    end=max(times)*n
    answer=float('inf')
    
    while(start<=end):
        middle=(start+end)//2
        sum_value=0
        
        for i in times:
            ram = middle % i
            sum_value+=(middle-ram)//i
            
        if(sum_value<n):
            start=middle+1
        elif(sum_value>=n):
            end=middle-1
            answer=min(answer,middle)
        
    return answer
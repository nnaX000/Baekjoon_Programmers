def solution(n, times):
    start=1
    end=max(times)*n
    answer=float('inf')
    
    while(start<=end):
        middle=(start+end)//2
        sum_value=0
        
        for i in times:
            ram = middle % i
            sum_value+=(middle-ram)//i #각 심사대마다 받을 수 있는 사람 수
            
        if(sum_value<n): #그게 n보다 작으면 시간이 부족한거니까 늘려주기
            start=middle+1
        elif(sum_value>=n): #그게 n보다 크면 최적값이 아닐수도 있으니 줄여주기
            end=middle-1
            answer=min(answer,middle)
        
    return answer
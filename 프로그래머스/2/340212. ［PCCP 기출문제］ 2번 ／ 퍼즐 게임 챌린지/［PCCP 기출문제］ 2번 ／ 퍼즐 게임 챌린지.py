def solution(diffs, times, limit):
    answer = 0
    start = 0
    end = 300000
    num = len(diffs)
    
    while(start<end):

        middle = (start+end)//2
        
        sum_value = 0
        
        for i in range(num):
            if(diffs[i]<=middle):
                sum_value+=times[i]
            else:
                incorrect = diffs[i]-middle
                
                if(i==0):
                    sum_value+=(incorrect*times[i])+times[i]
                else:
                    t = times[i]+times[i-1]
                    sum_value+=(t*incorrect)+times[i]
        
        #sum_value가 전체 제한시간보다 작은 경우
        if(sum_value<=limit):
            answer = middle
            end = middle
        else:
        #sum_value가 전체 제한시간보다 큰 경우
            start = middle

        if(end-start==1):
            break
                    
    return answer
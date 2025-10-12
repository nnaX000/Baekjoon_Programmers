def solution(sequence, k):
    length = len(sequence)
    start = 0
    end = -1
    sum_value = 0
    sum_value += sequence[0]
    answer = []
    
    while(True):
        if(sum_value<k):
            if(start<length-1):
                start+=1
                sum_value+=sequence[start]
            else:
                break
        elif(sum_value>k):
            if(end<length-1):
                end+=1
                sum_value-=sequence[end]
            else:
                break
        else:
            if(len(answer)==0 or answer[1]-answer[0]+1>start-end):
                answer = []
                if(end+1-start==0):
                    answer.append(start)
                    answer.append(start)
                else:
                    answer.append(end+1)
                    answer.append(start)

            if(start<length-1):
                start+=1
                sum_value+=sequence[start]
            else:
                break
                
    return answer
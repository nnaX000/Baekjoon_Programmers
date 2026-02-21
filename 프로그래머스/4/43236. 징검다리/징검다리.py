def solution(distance, rocks, n):
    answer = 0
    
    start=1
    end=distance
    
    rock=[0]
    rock.extend(rocks)
    rock.sort()
    rock.append(distance)
    
    while(start<=end):
        middle=(start+end)//2
        
        cnt=0
        prev=rock[0]
        
        for i in range(1,len(rock)):
            if(rock[i]-prev<middle):
                cnt+=1
            else:
                prev=rock[i]
                
        if(cnt<=n):
            answer=middle
            start=middle+1
        else:
            end=middle-1
            
    return answer
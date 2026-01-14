def solution(n, w, num):
    # n이 전체 상자 개수
    # w가 한 층에 쌓는 상자
    # num이 상자 번호
    
    boxs=[[] for _ in range(w)]
    left=True
    nb=1
    stand=0
    answer=0
    
    while(True):
        if(left):
            for i in range(w):
                if(nb==num):
                    stand=i
                boxs[i].append(nb)
                nb+=1
                if(n+1==nb):
                    break
            if(n+1==nb):
                break     
            left=False
        else:
            for i in range(w-1,-1,-1):
                if(nb==num):
                    stand=i
                boxs[i].append(nb)
                nb+=1
                if(nb==n+1):
                    break
            if(nb==n+1):
                break               
            left=True
            
    for i in range(len(boxs[stand])-1,-1,-1):
        if(boxs[stand][i]==num):
            break
        else:
            answer+=1   
                   
    return answer+1
#시작하기로 한 시각되면 시작
#기존에 진행중이던 과제 잇으면 그거 멈추고 새로운 과제 시작
# 과제 끝냇는데 새로 시작해야하는거랑 잠시 멈춰둔 과제 이렇게 있으면 새로 시작해야되는 과제부터 진행
from collections import deque

def solution(plans):
    answer = []
    dequee = deque()
    plans.sort(key = lambda x:x[1])
    
    for i in range(len(plans)):
        subject = plans[i][0]
        
        start = plans[i][1] #현재 과제 시각
        h,m = map(int,start.split(':'))
        
        cost = int(plans[i][2])
        
        if(i!=len(plans)-1):
            nx_start = plans[i+1][1] #다음 과제 시각
            nx_h,nx_m = map(int,nx_start.split(':'))

            time = (nx_h-h)*60 + (nx_m-m)

            if(time>cost):
                answer.append(subject)
                time-=cost
                while(time>0 and dequee):
                    s,r = dequee.pop()
                    nt = time-r
                    if(nt>=0):
                        answer.append(s)
                        time-=r
                    else:
                        dequee.append((s,r-time))
                        time=0
                        
            elif(time<cost):
                dequee.append((subject,cost-time))
            else:
                answer.append(subject)
        else:
            answer.append(subject)
    
    #나머지 큐에 있는거 다 순서대로 처리해서 넣기
    while(dequee):
        s,r = dequee.pop()
        answer.append(s)
        
    return answer
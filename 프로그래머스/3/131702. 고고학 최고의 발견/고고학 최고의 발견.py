from itertools import product

def solution(clockHands):
    answer = 100000
    row=len(clockHands)
    column=len(clockHands[0])
    
    candi=[0,1,2,3]
    result=0
    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    n_clock=[i[:] for i in clockHands]
    
    case=list(product(candi,repeat=column))
    
    for u in case:
        clockHands=[i[:] for i in n_clock]
        result=0
        for adx,a in enumerate(u):
            count=a
            result+=count

            clockHands[0][adx]=(clockHands[0][adx]+count)%4

            for k in range(4):
                nx=0+dx[k]
                ny=adx+dy[k]
                if(0<=nx<row and 0<=ny<column):
                    clockHands[nx][ny]=(clockHands[nx][ny]+count)%4

        for i in range(1,row):
            for j in range(column):
                if(clockHands[i-1][j]!=0):
                    count=(4-clockHands[i-1][j])%4
                    
                    result+=count
                    clockHands[i][j]=(clockHands[i][j]+count)%4

                    for k in range(4):
                        nx=i+dx[k]
                        ny=j+dy[k]

                        if(0<=nx<row and 0<=ny<column):
                            clockHands[nx][ny]=(clockHands[nx][ny]+count)%4
                            
        check=False
        for i in range(column):
            if(clockHands[row-1][i]!=0):
                check=True
                break
                
        if(not check):
            answer=min(answer,result)
                
    return answer
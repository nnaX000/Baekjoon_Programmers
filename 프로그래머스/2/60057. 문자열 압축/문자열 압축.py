from collections import deque
#절반까지만 보면 됨.
def solution(s):

    answer = 100000000
    
    if(len(s)>1):
        for i in range(1,(len(s)//2)+1):
            origin = s[:]
            dequee=deque()
            tmp=""
            candi=""

            for j in range(len(origin)):
                tmp+=origin[j]
                if len(tmp)==i:
                    dequee.append(tmp)
                    tmp=""

            if(len(tmp)>0):
                for j in tmp:
                    dequee.append(j)

            prev=dequee.popleft()
            count=1

            while(dequee):
                now=dequee.popleft()

                if(len(now)==i):
                    if(now==prev):
                        count+=1
                    else:
                        if(count>1):
                            candi+=str(count)
                            candi+=prev
                            
                            if(not dequee):
                                candi+=now
                            
                            if(dequee and len(dequee[0])<i):
                                prev="zz"
                                candi+=now
                        else:
                            candi+=prev
                            
                            if(not dequee):
                                candi+=now
                                
                            if(dequee and len(dequee[0])<i):
                                prev="zz"
                                candi+=now
                        
                        prev=now
                        count=1
                else:
                    if(count>1):
                        candi+=str(count)
                        candi+=prev
                        candi+=now
                        count=0
                        prev="zz"
                    else:
                        prev="zz"
                        candi+=now

            if(count>1):
                candi+=str(count)
                candi+=now 
            
            #print(candi)
            answer=min(answer,len(candi))
                
    else:
        answer=1
                    
    return answer
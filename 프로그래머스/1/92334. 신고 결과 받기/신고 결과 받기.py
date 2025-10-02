from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    call = defaultdict(set)
    mail = defaultdict(int)
    
    for i in id_list :
        mail[i] = 0
        
    for i in report :
        do, is_done = i.split(' ')
        call[is_done].add(do)
        
    for key,value in call.items():
        if(len(value)>=k):
            for i in value:
                mail[i]+=1
                
    for i in mail.values():
        answer.append(i)
        
    return answer
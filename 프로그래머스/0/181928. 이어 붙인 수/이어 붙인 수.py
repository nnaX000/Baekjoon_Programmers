def solution(num_list):
    odd = ''
    jjak = ''
    
    for i in num_list:
        if(i%2==1):
            odd+=str(i)
        else:
            jjak+=str(i)
            
    answer = int(odd)+int(jjak)
    return answer
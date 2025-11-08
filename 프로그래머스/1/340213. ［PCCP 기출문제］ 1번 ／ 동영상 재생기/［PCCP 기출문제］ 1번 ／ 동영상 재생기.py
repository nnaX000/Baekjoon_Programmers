def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    op_start_m, op_start_s = map(int,op_start.split(':'))
    op_end_m, op_end_s = map(int,op_end.split(":"))
    c_m, c_s = map(int,pos.split(":")) #현재 분, 초
    video_m, video_s = map(int,video_len.split(":"))
    total = video_m*60+video_s
    
    for i in commands:
        if(op_start_m*60+op_start_s<=c_m*60+c_s<=op_end_m*60+op_end_s):
                c_m = op_end_m
                c_s = op_end_s
                
        if(i=="prev"):
            if(c_m*60+c_s>10):
                c_s-=10
                if(c_s<0):
                    c_s=60+c_s
                    c_m-=1
            else:
                c_m,c_s=0,0
                
        elif(i=="next"):
            if(total-(c_m*60+c_s)>10):
                c_s+=10
                if(c_s>=60):
                    c_m+=1
                    c_s=c_s-60
            else:
                c_m = video_m
                c_s = video_s
    
    if(op_start_m*60+op_start_s<=c_m*60+c_s<=op_end_m*60+op_end_s):
            c_m = op_end_m
            c_s = op_end_s
                
    c_m=str(c_m)
    c_s=str(c_s)
    
    if(len(c_m)==1):
        c_m="0"+c_m
    if(len(c_s)==1):
        c_s="0"+c_s
        
    answer+=str(c_m)+":"+str(c_s)
    return answer
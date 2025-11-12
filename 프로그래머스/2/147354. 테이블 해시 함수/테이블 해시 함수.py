def solution(data, col, row_begin, row_end):
    answer = 0
    candi = []
    
    data.sort(key=lambda x:x[0],reverse=True)
    data.sort(key=lambda x:x[col-1])
    
    for i in range(row_begin-1,row_end):
        tmp = 0
        for j in range(len(data[i])):
            tmp+=(data[i][j]%(i+1))
        candi.append(tmp)
        
    answer=candi[0]
    for i in range(1,len(candi)):
        answer=answer^candi[i]
        
    return answer
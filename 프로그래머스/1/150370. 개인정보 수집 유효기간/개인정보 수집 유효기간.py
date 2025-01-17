def solution(today, terms, privacies):
    answer = []
    today_array=[]
    today_array=list(map(int,today.split('.')))
    
    for idx,i in enumerate(privacies):
        date=[]
        collections=i.split(' ')
        date=list(map(int,collections[0].split('.')))
        types=collections[1]
        print(date)
        print(types)
        for j in terms:
            if(j[0]==types):
                lasting=[]
                lasting=j.split(' ')
                break
        summ=date[1]+int(lasting[1])
        print("summ",summ)
        while(summ>12):
            date[0]+=1
            print("date[0]",date[0])
            summ-=12
        date[1]=summ
        # if (date[1]+int(lasting[1])>12):
        #     tmp=int(lasting[1])//12
        #     date[0]+=tmp
        #     date[1]%=12 #지속해도 되는 기간
        print("지속해도 되는 기간",date)
        if(date[0]<today_array[0]):
            answer.append(idx+1)
            continue
        if(date[0]==today_array[0] and date[1]<today_array[1]):
            answer.append(idx+1)
            continue
        if(date[0]==today_array[0] and date[1]==today_array[1] and date[2]<=today_array[2]):
            answer.append(idx+1)
    return answer
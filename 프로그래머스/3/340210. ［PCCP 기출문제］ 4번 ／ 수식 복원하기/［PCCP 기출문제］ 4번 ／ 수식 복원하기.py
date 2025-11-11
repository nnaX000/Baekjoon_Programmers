def solution(expressions):
    #2진법 -> 0,1
    answer = []
    complete = []
    test = []
    result = 0
    num_clus = ""
    max_num = 0
    possible = []
    
    for i in range(len(expressions)):
        num_1,tool,num_2,equal,result = expressions[i].split(' ')
        if(result!="X"):
            complete.append([num_1,num_2,result,tool])
            num_clus+=num_1
            num_clus+=num_2
            num_clus+=result
        else:
            test.append([num_1,num_2,tool])
            num_clus+=num_1
            num_clus+=num_2
        
    for i in num_clus:
        max_num = max(int(i),max_num)
        
    for i in range(max_num+1,10):
        check=True
        
        for j in range(len(complete)):
            num_1,num_2,result,tool = complete[j][0],complete[j][1],complete[j][2],complete[j][3]
            candi = [int(num_1,i),int(num_2,i),int(result,i)]
            
            if(tool=="+"):
                if(candi[0]+candi[1]!=candi[2]):
                    check=False
                    break
            elif(tool=="-"):
                if(candi[0]-candi[1]!=candi[2]):
                    check=False
                    break
                    
        if(check):
            possible.append(i)
    
    print(possible)
            
    for i in range(len(test)):
        num_1,num_2,tool = test[i][0],test[i][1],test[i][2]
        candi = [num_1,num_2,tool]
        x = ""
        compare = 0
        check = True
            
        for j in range(len(possible)):
            anw_f = ""
            
            if(tool=="+"):
                anw = int(num_1,possible[j]) + int(num_2,possible[j])
            else:
                anw = int(num_1,possible[j]) - int(num_2,possible[j])

            while(anw>0):
                anw_f=str(anw%possible[j])+anw_f
                anw//=possible[j]

            if(j==0):
                compare = anw_f
            else:
                if(anw_f!=compare):
                    check=False
                    anw_f="?"
                    break
        
        if(len(anw_f)==0):
            anw_f = 0
            
        x+=num_1+" "
        x+=tool+" "
        x+=num_2+" = "
        x+=str(anw_f)
        answer.append(x)
                
    return answer
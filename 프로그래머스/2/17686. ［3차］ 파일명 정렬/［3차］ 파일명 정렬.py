def solution(files):
    answer = []
    tmp= [[] for i in range(len(files))]
    for i in range(len(files)):
        tmp[i].append(i) #idx 0
        pos = 0
        head = ""
        number = ""
        tail = ""
        
        #헤드 구하기 idx 1
        for j in range(pos,len(files[i])):
            if(ord(files[i][j])<48 or ord(files[i][j])>57):
                head+=files[i][j]
                pos = j
            else:
                break

        tmp[i].append(head.lower())
        
        #넘버 구하기 idx 2
        for j in range(pos+1,len(files[i])):
            if(48<=ord(files[i][j])<=57):
                number+=files[i][j]
                pos = j
            else:
                break
                
        n_number = int(number)
        tmp[i].append(n_number)
               
        #테일 구하기 idx 3
        tmp[i].append(files[i][pos+1:])
        
    tmp.sort(key = lambda x:x[2])
    tmp.sort(key = lambda x:x[1])
        
    for i in range(len(tmp)):
        pos = tmp[i][0]
        answer.append(files[pos])
               
    return answer
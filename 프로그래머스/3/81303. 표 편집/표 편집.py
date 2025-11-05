from collections import deque

def solution(n, k, cmd):
    answer = ["O" for i in range(n)]
    prev = [i-1 for i in range(n)]
    nxt = [i+1 for i in range(n)]
    
    current = k
    latest = deque()
    
    for i in cmd:
        if(i[0] == "D") or (i[0] == "U"):
            order,num = i.split(' ')
            num = int(num)
        else:
            order = i
        
        if(order == "U"):
            for j in range(num):   
                current = prev[current]
        elif(order == "D"):
            for j in range(num):
                current = nxt[current]         
        elif(order == "C"):
            answer[current] = "X" # 현재 선택한 행 삭제로 바꿈
            latest.append((current,prev[current],nxt[current])) # 제일 최근에 삭제한 행에 선택한 행 넣음
            
            if prev[current] != -1:
                nxt[prev[current]] = nxt[current]
            if nxt[current] != n:
                prev[nxt[current]] = prev[current]
            
            if(nxt[current]==n):
                current=prev[current]
            else:
                current=nxt[current]
        else:
            idx,p,n_ = latest.pop()
            answer[idx]="O"
            
            if p != -1:
                nxt[p] = idx
            if n_ != n:
                prev[n_] = idx
            
    
    return ''.join(answer)
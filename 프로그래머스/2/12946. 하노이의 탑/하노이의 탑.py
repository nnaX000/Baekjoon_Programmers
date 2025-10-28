from collections import deque

def solution(n):
    answer = [] #[이전 기둥 id, 이후 기둥 id]
    
    def hanoi(num,start,mid,end):
        if(num==1):
            answer.append([start,end])
            return
        
        hanoi(num-1,start,end,mid)#1단계
        answer.append([start,end])#2단계
        hanoi(num-1,mid,start,end)#3단계
    
    hanoi(n,1,2,3)
    
    return answer
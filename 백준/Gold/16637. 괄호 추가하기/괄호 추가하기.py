import sys
from collections import deque

input=sys.stdin.readline

# 괄호 안에는 연산자가 하나만 들어 있어야
# 연산자 우선순위는 모두 동일하기 때문에, 수식을 계산할 때는 왼쪽에서부터 순서대로 계산

answer=float('-inf')

def dfs(start,array):
    global candi
    global arr

    if(start>=len(candi)):
        arr.append(array[:])
        return
    
    dfs(start+2,array)

    for i in range(start,len(candi)):
        array.append(candi[i])
        dfs(i+2,array)
        array.pop()

N=int(input())
S=input()

candi=[]
arr=[]

for i in range(0,N-2,2):
    candi.append(i)

dfs(0,[])

s_arr=set(tuple(i) for i in arr)
s_arr=list(list(i) for i in s_arr)
s_arr.append([])

for i in range(len(s_arr)):
    sett=s_arr[i]
    S_t=list(S[:])

    #괄호로 먼저 계산해야되는거 먼저 일괄 치환
    for j in sett:
        j=int(j)
        if(S_t[j+1]=="*"):
            S_t[j]=int(S_t[j])*int(S_t[j+2])
            S_t[j+1]=""
            S_t[j+2]=""
        elif(S_t[j+1]=="+"):
            S_t[j]=int(S_t[j])+int(S_t[j+2])
            S_t[j+1]=""
            S_t[j+2]=""
        elif(S_t[j+1]=="-"):
            S_t[j]=int(S_t[j])-int(S_t[j+2])
            S_t[j+1]=""
            S_t[j+2]=""

    pre=deque(S_t)
    nxt=deque()

    while(pre):
        tmp=pre.popleft()
        if(tmp!="" and tmp!='\n'):
            nxt.append(tmp)

    idx=0
    sv=int(nxt.popleft())

    #계산
    while(nxt):
        op=nxt.popleft()
        k=int(nxt.popleft())

        if(op=="+"):
            sv+=k
        elif(op=="*"):
            sv*=k
        elif(op=="-"):
            sv-=k
    
    answer=max(answer,sv)

print(answer) 
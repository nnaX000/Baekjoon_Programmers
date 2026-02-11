import sys
from collections import deque
from itertools import combinations

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
    
    #현재 후보 미선택
    dfs(start+1,array)

    #현재 후보 선택
    array.append(candi[start])
    dfs(start+2,array)
    array.pop()

N=int(input())
S=input()

candi=[]
arr=[]

for i in range(0,N-2,2):
    candi.append(i)

dfs(0,[])

for i in range(len(arr)):
    sett=arr[i]
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
    snxt=deque()

    while(pre):
        tmp=pre.popleft()
        if(tmp!="" and tmp!='\n'):
            nxt.append(tmp)

    n1=int(nxt.popleft())

    # 곱하기 먼저 계산
    while(nxt):
        op=nxt.popleft()
        n2=int(nxt.popleft())

        if(op=="*"):
            n1=n1*n2
        else:
            snxt.append(n1)
            snxt.append(op)
            n1=n2

    if(not snxt or snxt[-1]=="+" or snxt[-1]=="-"):
        snxt.append(n1)

    #나머지 계산
    sv=int(snxt.popleft())
    
    while(snxt):
        op=snxt.popleft()
        k=int(snxt.popleft())

        if(op=="+"):
            sv+=k
        elif(op=="-"):
            sv-=k
    
    answer=max(answer,sv)

print(answer)  
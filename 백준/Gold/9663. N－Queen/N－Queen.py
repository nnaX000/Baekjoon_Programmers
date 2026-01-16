import sys

input=sys.stdin.readline

N=int(input())

left=[False for _ in range(35)]
right=[False for _ in range(35)]
column=[False for _ in range(16)]

answer=0

def dfs(x,count,left,right,column):
    global answer

    if(count==N):
        answer+=1

    for i in range(N): # x라는 행의 열을 일일히 돌리는 중
        if(not column[i] and not right[x-i] and not left[x+i]):
            right[x-i]=True
            left[x+i]=True
            column[i]=True
            dfs(x+1,count+1,left,right,column)
            right[x-i]=False
            left[x+i]=False
            column[i]=False

dfs(0,0,left,right,column)

print(answer)
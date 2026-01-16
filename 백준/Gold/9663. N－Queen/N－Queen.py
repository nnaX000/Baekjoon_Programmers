import sys

input=sys.stdin.readline

N=int(input())

left=[0 for _ in range(35)]
right=[0 for _ in range(35)]
column=[0 for _ in range(16)]

answer=0

def dfs(x,count,left,right,column):
    global answer

    if(count==N):
        answer+=1

    for i in range(N): # x라는 행의 열을 일일히 돌리는 중
        check=True

        #열 체크
        if(column[i]!=0):
            check=False
        
        #오른쪽 방향 대각선 체크
        if(check):
            if(right[x-i]!=0):
                check=False

        #왼쪽 방향 대각선 체크
        if(check):
            if(left[x+i]!=0):
                check=False

        if(check):
            right[x-i]+=1
            left[x+i]+=1
            column[i]+=1
            dfs(x+1,count+1,left,right,column)
            right[x-i]-=1
            left[x+i]-=1
            column[i]-=1

dfs(0,0,left,right,column)

print(answer)
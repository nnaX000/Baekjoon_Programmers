import sys

T=int(sys.stdin.readline().rstrip())

def dfs(num,sum_value):
    global method
    if(sum_value==num):
        method+=1
        return
    
    if(sum_value+1<=num):
        sum_value+=1
        dfs(num,sum_value)
        sum_value-=1

    if(sum_value+2<=num):
        sum_value+=2
        dfs(num,sum_value)
        sum_value-=2

    if(sum_value+3<=num):
        sum_value+=3
        dfs(num,sum_value)
        sum_value-=3

    return method

for i in range(T):
    tmp=int(sys.stdin.readline().rstrip())
    method=0
    sum_value=0
    result=dfs(tmp,sum_value)
    print(result)
import sys

N,S=map(int,sys.stdin.readline().rstrip().split(' '))

array=list(map(int,sys.stdin.readline().rstrip().split(' ')))

answer=0

def dfs(start,sum_value,tmp):
    global answer

    if(sum_value==S and tmp):
        answer+=1
        
    for i in range(start,N):
        sum_value+=array[i]
        tmp.append(i)
        dfs(i+1,sum_value,tmp)
        sum_value-=array[i]
        tmp.pop()

tmp=[]

dfs(0,0,tmp)

print(answer)
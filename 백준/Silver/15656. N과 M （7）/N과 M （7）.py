import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))
array.sort()

answer=[]

def dfs(array,tmp):
    global answer
    if(len(tmp)==M):
        print(*tmp)
        return
    for i in range(len(array)):
        tmp.append(array[i])
        dfs(array,tmp)
        tmp.pop()

tmp=[]
dfs(array,tmp)
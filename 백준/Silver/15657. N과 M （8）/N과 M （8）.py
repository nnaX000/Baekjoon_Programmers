import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))
array.sort()

def dfs(start,array,tmp):
    if(len(tmp)==M):
        print(*tmp)
        return

    for i in range(start,len(array)):
        tmp.append(array[i])
        dfs(i,array,tmp)
        tmp.pop()

start=0
tmp=[]
dfs(start,array,tmp)
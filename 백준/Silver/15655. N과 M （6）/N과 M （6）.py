import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

array=list(map(int,sys.stdin.readline().rstrip().split(' ')))

array.sort()

#순열은 visited 써야하고 조합은 start

def dfs(start,array,tmp):
    if(len(tmp)==M):
        print(*tmp)
        return
    
    for i in range(start+1,len(array)):
        tmp.append(array[i])
        dfs(i,array,tmp)
        tmp.pop()

tmp=[]
dfs(-1,array,tmp)
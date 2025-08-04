import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

answer=set()

def dfs(array, tmp):
    global answer
    if(len(tmp)==M):
        answer.add(tuple(tmp[:]))
        return
    
    for i in range(len(array)):
        tmp.append(array[i])
        dfs(array, tmp)
        tmp.pop()

    return answer

array=[i+1 for i in range(N)]

start=0

tmp=[]

visited=[False for i in range(M)]

result=dfs(array,tmp)

result=list(result)

result.sort()

for i in result:
    print(*i)
import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))
array.sort()

answer=set()

def dfs(array,tmp):
    global answer
    if(len(tmp)==M):
        answer.add(tuple(tmp[:]))
        return
    for i in range(len(array)):
        tmp.append(array[i])
        dfs(array,tmp)
        tmp.pop()

tmp=[]
dfs(array,tmp)

answer=list(answer)
answer.sort()

for i in answer:
    print(*i)
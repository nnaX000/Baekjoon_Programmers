import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

answer=set()

def dfs(array,start,tmp):
    global answer
    if(len(tmp)==M):
        answer.add(tuple(tmp[:]))
        return

    for i in range(start,len(array)):
        tmp.append(array[i])
        dfs(array,i,tmp)
        tmp.pop()

array=[i+1 for i in range(N)]

array.sort()

start=0

tmp=[]

dfs(array,start,tmp)

answer=list(answer)

answer.sort()

for i in answer:
    print(*i)
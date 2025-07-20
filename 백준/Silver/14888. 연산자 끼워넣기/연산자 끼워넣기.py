import sys
import itertools

A=[]
operator=[]

N=int(sys.stdin.readline().rstrip())

A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
operator=list(map(int,sys.stdin.readline().rstrip().split(' ')))
operators=[]

min_value=[float('inf')]
max_value=[-1*float('inf')]

for idx,i in enumerate(operator):
    tmp=""
    if(idx==0):
        tmp="+"
    elif(idx==1):
        tmp="-"
    elif(idx==2):
        tmp="x"
    else:
        tmp="/"

    for j in range(i):
        operators.append(tmp)

visited=[False for i in range(len(operators))]
path=[]
answer=[]

def dfs(path,length):
    if(len(path)==length):
        answer.append(path[:])

    for i in range(len(operators)):
        if(visited[i]):
            continue
        if(i>0 and operators[i]==operators[i-1] and not visited[i-1]):
            continue
        path.append(operators[i])
        visited[i]=True
        dfs(path,length)
        visited[i]=False
        path.pop()
    

dfs(path,N-1)

for i in answer:
    start=A[0]
    for jdx,j in enumerate(i):
        if (j=="+"):
            start+=A[jdx+1]
        elif (j=="-"):
            start-=A[jdx+1]
        elif (j=="x"):
            start*=A[jdx+1]
        else:
            if(start<0):
                start*=-1
                start//=A[jdx+1]
                start*=-1
            else:
                start//=A[jdx+1]
    
    if(start<min_value[0]):
        min_value[0]=start
    if(start>max_value[0]):
        max_value[0]=start

print(max_value[0])
print(min_value[0])

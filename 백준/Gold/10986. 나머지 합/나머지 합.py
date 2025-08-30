import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

answer=0

start,end=0,0

sum_value=[]

tmp=0

dic={}

for i in range(N):
    tmp+=A[i]
    sum_value.append(tmp)

for i in sum_value:
    tmp=i%M
    if(tmp in dic):
        dic[tmp]+=1
    else:
        dic[tmp]=1

for key,value in dic.items():
    if(key==0):
        answer+=value

    answer+=(value*(value-1))//2

print(answer)
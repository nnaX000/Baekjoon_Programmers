import sys

N,S=map(int,sys.stdin.readline().rstrip().split(' '))
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))

start,end=0,0

min_len=200000

sum_value=0

while(True):
    if(sum_value>=S):
        min_len=min(min_len,end-start)
        sum_value-=A[start]
        start+=1
    elif(end==N):
        break
    elif(sum_value<S):
        sum_value+=A[end]
        end+=1

if(min_len==200000):
    print(0)
else:
    print(min_len)
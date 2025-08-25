import sys
import itertools

N=int(sys.stdin.readline().rstrip())

S=list(map(int,sys.stdin.readline().rstrip().split(' ')))

value=[-1 for i in range(2000000)]

value[0]=1

for i in range(1,len(S)+1):
    result=list(itertools.combinations(S,i))
    for j in result:
        sum_value=sum(j)
        if(value[sum_value]==-1):
            value[sum_value]=1

for idx,i in enumerate(value):
    if(i == -1):
        print(idx)
        break
import sys
from collections import defaultdict

input=sys.stdin.readline

nums=defaultdict(int)
idx=0
answer=[]

N=int(input())
X=list(map(int,input().split(' ')))

n_X=sorted(X)

for i in n_X:
    if(i not in nums):
        nums[i]=idx
        idx+=1

for i in X:
    answer.append(nums[i])

print(*answer)
import sys
from collections import defaultdict

N=int(sys.stdin.readline().rstrip())
tang=list(map(int,sys.stdin.readline().rstrip().split(' ')))
nums=defaultdict(int)
max_value=float('-inf')

left=0
right=0
count=0

for idx,i in enumerate(tang):
    if(nums[i]==0):
        nums[i]+=1
        count+=1
    else:
        nums[i]+=1

    if(count>2):
        while(count>2):
            nums[tang[left]]-=1

            if(nums[tang[left]]==0):
                count-=1

            left+=1

    max_value=max(max_value,idx-left+1)

print(max_value)
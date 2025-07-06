import sys

nums=[]

nums=list(map(int,sys.stdin.readline().strip().split(' ')))

nums.sort()

for i in range(3):
    print(nums[i],end=" ")

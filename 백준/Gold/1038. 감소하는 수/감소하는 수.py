from collections import deque

N=int(input())
count=-1
nums=[]

def dfs(current):
    last=int(current[-1])

    for i in range(last):
        temp=current
        temp+=str(i)
        nums.append(int(temp))
        dfs(temp)

for i in range(10):
    nums.append(i)
    dfs(str(i))

aligned_nums=sorted(nums)

if(N>len(nums)-1):
    print(-1)
else:
    print(aligned_nums[N])


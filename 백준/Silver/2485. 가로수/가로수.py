import math
num=int(input())
first=int(input())
nums=[first]
array=[]
answer=0
for i in range(1,num):
    tmp=int(input())
    nums.append(tmp)
    array.append(nums[i]-nums[i-1])
a=array[0]
for i in range(1,len(array)):
    a=math.gcd(a,array[i])
for i in range(len(array)):
    answer+=array[i]//a-1
print(answer)
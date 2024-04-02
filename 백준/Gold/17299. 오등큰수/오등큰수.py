from collections import deque
dequee=deque()
num=int(input())
array=list(map(int,input().split(' ')))
nums=[0 for i in range(1000001)]
answer=[-1 for i in range(num)]
idx=deque()
dequee.append(array[0])
idx.append(0)
for i in array:
    nums[i]+=1
for index,i in enumerate(array):
    if(index>0):
        if(len(dequee)>0 and nums[dequee[-1]]<nums[i]):
            while(len(dequee)>0 and nums[dequee[-1]]<nums[i]):
                dequee.pop()
                a=idx.pop()
                answer[a]=i
            dequee.append(i)
            idx.append(index)
        else:
            dequee.append(i)
            idx.append(index)

for i in answer:
    print(i,end=" ")
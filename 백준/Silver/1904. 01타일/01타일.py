num=int(input())
array=[0]*(num+1)
array[0]=1
array[1]=1
answer=0
for i in range(2,num+1):
    temp=array[i-1]+array[i-2]
    if(temp>=15746):
        array[i]=temp%15746
    else:
        array[i]=temp
print(array[num])
# 1 1 2 3 5
import sys
import math
set={0}
tmp=0
min,max=map(int,sys.stdin.readline().split())
real_min=min
for i in range(2,int(math.sqrt(max))+1):
    min=real_min
    tmp=min//(i*i)
    if(tmp>0 and min%(i*i)!=0):
        min+=(i*i)-(min%(i*i))
    elif (tmp > 0 and min % (i * i) == 0):
        min=real_min
    else:
        if(i*i<=max):
            min=i*i
    for j in range(min,max+1,i*i):
            #print("j",j)
            set.add(j)

#print(set)
print(max-real_min+1-len(set)+1)


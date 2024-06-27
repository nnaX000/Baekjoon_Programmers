import sys
min,order=map(int, sys.stdin.readline().split())
array=[0]*(min+1)#0소수 1소수아님
array[0]=1
array[1]=1
def ce(min,array,order):
    count=0
    for i in range(2,min+1):
        if(array[i]==0):
            array[i]=1
            count+=1
            #print(i, count)
            if (count == order or sum(array)==min+1):
                return i
            for j in range(i+i,min+1,i):
                if(array[j]==0):
                    array[j]=1
                    count+=1
                    #print(j,count)
                    if(count==order or sum(array)==min+1):
                        return j
print(ce(min,array,order))

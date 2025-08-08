import sys

N=int(sys.stdin.readline().rstrip())
array=list(map(int,sys.stdin.readline().rstrip().split(' ')))
check=False
stand=0

for i in range(len(array)-2,-1,-1):
    if(array[i+1]-array[i]<0):
        check=True
        stand=i
        break

if(not check):
    print(-1)
else:
    for i in range(len(array)-1,stand,-1):
        if(array[i]<array[stand]):
            array[i],array[stand]=array[stand],array[i]
            break

    array[stand+1:] = sorted(array[stand+1:],reverse=True)

    print(*array)
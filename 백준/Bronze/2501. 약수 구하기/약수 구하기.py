import sys

N, K = map(int,sys.stdin.readline().rstrip().split(' '))

array=[]

for i in range(1,int(N**(1/2))+1):
    if(N%i==0):
        array.append(i)
        if(i!=N//i):
            array.append(N//i)

array.sort()

print(array[K-1] if len(array)>=K else 0)
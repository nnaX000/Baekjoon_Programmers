import sys

n=int(sys.stdin.readline().rstrip())

array=[0 for i in range(1001)]

array[1]=1
array[2]=3

for i in range(3,len(array)):
    array[i]=(array[i-2]*2)+array[i-1]

print(array[n]%10007)
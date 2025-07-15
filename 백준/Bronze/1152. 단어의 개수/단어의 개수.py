import sys

array=list(sys.stdin.readline().rstrip().split(' '))

count=0

for i in array:
    if(i==''):
        count+=1

print(len(array)-count)
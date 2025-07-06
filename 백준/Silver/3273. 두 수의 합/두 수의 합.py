import sys

n=int(sys.stdin.readline().strip())

array=list(map(int,sys.stdin.readline().strip().split(' ')))

x=int(sys.stdin.readline().strip())

array_set=dict()

for i in range(n):
    array_set[array[i]]=i

answer=0

for idx,i in enumerate(array_set) :
    tmp = x-i

    if(tmp in array_set and array_set[tmp]<idx):
        answer+=1

print(answer)
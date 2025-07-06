import sys
import itertools

N=int(sys.stdin.readline().strip())
array=list(map(int,sys.stdin.readline().strip().split(' ')))

array.sort()

target=1

for i in array:
    if(target<i):
        break
    target+=i

print(target)
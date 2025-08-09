import sys
from itertools import combinations

while(True):
    array=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    if(array[0]==0):
        break
    else:
        array=array[1:]
        results=combinations(array,6)
        for i in results:
            print(*i)
    print()
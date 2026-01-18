import sys
from collections import defaultdict,deque

sys.setrecursionlimit(10**6)

input=sys.stdin.readline
array=[]

while(True):
    try:
        array.append(int(input()))
    except:
        break

def post(start,end):
    if(start>=end):
        return
    
    root=array[start]
    idx=start+1
    while(idx<end and array[idx]<root):
        idx+=1

    post(start+1,idx)
    post(idx,end)
    print(root)

post(0,len(array))
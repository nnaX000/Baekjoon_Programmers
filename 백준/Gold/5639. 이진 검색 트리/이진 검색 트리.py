import sys

input=sys.stdin.readline

sys.setrecursionlimit(10**6)

arr=[]

while(True):
    try:
        arr.append(int(input()))
    except:
        break

def binary(start,end):
    #print(start,end)

    if(start>=end):
        return

    root=arr[start]
    idx=start+1

    while(idx<end and arr[idx]<root):
        idx+=1

    binary(start+1,idx) #왼쪽
    binary(idx,end) #오른쪽
    print(root)

binary(0,len(arr))
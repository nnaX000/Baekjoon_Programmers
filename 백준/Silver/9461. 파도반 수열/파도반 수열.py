import sys

T=int(sys.stdin.readline().rstrip())
array=[1,1,1,2,2,3,4,5,7,9]

tmp=[]

for i in range(T):
    N=int(sys.stdin.readline().rstrip())
    tmp.append(N)

max_value=max(tmp)

left=5
right=9

for i in range(max_value-9):
    array.append(array[left]+array[right])
    left+=1
    right+=1

for i in tmp:
    print(array[i-1])
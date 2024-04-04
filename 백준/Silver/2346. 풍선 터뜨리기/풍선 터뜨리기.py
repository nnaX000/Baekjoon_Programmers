from collections import deque
num=int(input())
array=list(map(int,input().split(' ')))
for i in range(num):
    array[i]=[i+1,array[i]]
array=deque(array)
size=0
answer=[]
while(array):
    if(size>=0):
        for i in range(size-1):
            a=array.popleft()
            array.append(a)
        target=array.popleft()
        answer.append(target[0])
        size=target[1]
    else:
        for i in range(abs(size)-1):
            a = array.pop()
            array.appendleft(a)
        target = array.pop()
        answer.append(target[0])
        size = target[1]
for i in answer:
    print(i,end=" ")
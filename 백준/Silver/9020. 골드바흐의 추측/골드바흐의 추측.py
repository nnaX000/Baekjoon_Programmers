import sys
array=[0]*10001#0은 소수 1은 소수아님
array[0]=1
array[1]=1
for i in range(2,5001):
    for j in range(i+i,10001,i):
            array[j]=1

#print(array)

num=int(sys.stdin.readline())
for i in range(num):
    tmp=int(sys.stdin.readline())
    for j in range(tmp//2,1,-1):
        if(array[j]==0 and array[tmp-j]==0):
            print(j,tmp-j)
            break
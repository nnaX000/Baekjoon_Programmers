import sys
box,order=map(int,sys.stdin.readline().split())
array=[0]*(box+1)
#박스 개수 | 명령어 개수
for i in range(order):
    a,b,x=map(int,sys.stdin.readline().split())
    for j in range(a,b+1):
        array[j]=x

for i in range(len(array)):
    if(i!=0):
        print(array[i],end=" ")
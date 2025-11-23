import sys

N=int(sys.stdin.readline().rstrip())
A=list(map(int,sys.stdin.readline().rstrip().split(' ')))
L=[]
L.append(A[0])

for i in range(1,len(A)):
    if(L[-1]<A[i]):
        L.append(A[i])
    else:
        start=0
        end=len(L)-1

        while(start<=end):
            middle = (start+end)//2

            if(L[middle]<A[i]):
                start=middle+1
            else:
                end=middle-1

        L[start]=A[i]
        
print(len(L))
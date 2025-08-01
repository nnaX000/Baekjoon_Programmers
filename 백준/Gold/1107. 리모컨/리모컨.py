import sys

N=int(sys.stdin.readline().rstrip())
M=int(sys.stdin.readline().rstrip())
number=[0,1,2,3,4,5,6,7,8,9]
if(M>0):
    dys=list(map(int,sys.stdin.readline().rstrip().split(' ')))
else:
    dys=[]

closest=[]
direct=abs(100-N)

for i in range(1000001):
    utter=True
    tmp=str(i)
    for j in tmp:
        if(int(j) in dys):
            utter=False
            break
    if(utter):
        direct=min(direct,abs(N-i)+len(tmp))

print(direct)
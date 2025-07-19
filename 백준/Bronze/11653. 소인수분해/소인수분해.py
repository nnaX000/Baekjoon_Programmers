import sys

N=int(sys.stdin.readline().rstrip())

i=2
answer=[]

while(i*i<=N):
    while(N%i==0):
        answer.append(i)
        N//=i
    i+=1

if(N>1):
    answer.append(N)

for i in answer:
    print(i)
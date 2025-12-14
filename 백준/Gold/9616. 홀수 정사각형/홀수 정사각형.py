import sys

while(True):
    m,n=map(int,sys.stdin.readline().rstrip().split(' '))
    if(m==0 and n==0):
        break
    answer=0
    for i in range(1,min(m,n)+1,2):
        answer+=(m-i+1)*(n-i+1)*i
    print(answer)
    
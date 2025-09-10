import sys

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    a,b=map(int,sys.stdin.readline().rstrip().split(' '))
    last = pow(a , b, 10)   
    print(10 if last == 0 else last) 
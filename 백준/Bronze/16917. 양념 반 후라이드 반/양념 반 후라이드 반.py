import sys

A,B,C,X,Y= map(int,sys.stdin.readline().rstrip().split(' '))

answer=float('inf')
max_value=max(X,Y)

for i in range(max_value+1):
    mild=A * max(0,X-i)
    sauce=B * max(0,Y-i)
    half=C * (i*2)

    if(mild+sauce+half<answer):
        answer=mild+sauce+half

print(answer)
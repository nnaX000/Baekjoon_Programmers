import sys

min_value=0

N=int(sys.stdin.readline().strip())

A=list(map(int,sys.stdin.readline().strip().split(' ')))
B=list(map(int,sys.stdin.readline().strip().split(' ')))

A.sort()
B.sort(reverse=True)

for i in range(len(A)):
    min_value+=A[i]*B[i]

print(min_value)
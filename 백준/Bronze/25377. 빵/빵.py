import sys

N=int(sys.stdin.readline().rstrip())
min_value=float('inf')

for i in range(N):
    A,B=map(int,sys.stdin.readline().rstrip().split(' '))
    if(A<=B):
        min_value=min(min_value,B)

print(min_value if min_value!=float('inf') else -1)
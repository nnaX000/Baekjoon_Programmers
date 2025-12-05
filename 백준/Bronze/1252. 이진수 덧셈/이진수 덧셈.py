import sys

a,b=sys.stdin.readline().rstrip().split(' ')

n_a=int(a,2)
n_b=int(b,2)
result=n_a+n_b
result=bin(result)

print(result[2:])
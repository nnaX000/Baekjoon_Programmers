import sys

N=int(sys.stdin.readline().rstrip())

array=list(map(int,sys.stdin.readline().rstrip().split(' ')))

v=int(sys.stdin.readline().rstrip())

print(array.count(v))
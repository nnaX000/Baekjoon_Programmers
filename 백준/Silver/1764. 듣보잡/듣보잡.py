import sys

N,M=map(int,sys.stdin.readline().rstrip().split(' '))

hear_x=set()
look_x=set()

for i in range(N):
    hear_x.add(sys.stdin.readline().rstrip())

for i in range(M):
    look_x.add(sys.stdin.readline().rstrip())

result=sorted(list(hear_x & look_x))

print(len(result))

for i in result:
    print(i)
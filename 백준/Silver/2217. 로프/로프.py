import sys

N=int(input())

rope=[]
max_value=0

for i in range(N):
    rope.append(int(sys.stdin.readline()))

rope.sort()

for i in range(N):
    max_value=max(max_value,rope[i]*(N-i))

print(max_value)
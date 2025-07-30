import sys

S=int(sys.stdin.readline().rstrip())
sum=0
num=0

while(sum<=S):
    num+=1
    sum+=num

print(num-1)
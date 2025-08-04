import sys

N=int(sys.stdin.readline().rstrip())

answer=0

j=len(str(N))-1

while(N!=0):
    zero_base=N-(10**j)+1

    answer+=zero_base*len(str(N))

    j-=1

    N-=zero_base

print(answer)
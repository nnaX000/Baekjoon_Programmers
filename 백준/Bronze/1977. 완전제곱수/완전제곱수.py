import sys
import math

M=int(sys.stdin.readline().rstrip())
N=int(sys.stdin.readline().rstrip())

M_range=math.ceil(math.sqrt(M))
N_range=math.floor(math.sqrt(N))

sum_value=0
min_value=float('inf')

for i in range(M_range,N_range+1):
    sum_value+=i*i
    if min_value==float('inf'):
        min_value=i*i

if(min_value!=float('inf')):
    print(sum_value)
    print(min_value)
else:
    print(-1)
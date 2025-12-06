import sys

N=int(sys.stdin.readline().rstrip())
tropy=[]

left=0
right=0

for i in range(N):
    tropy.append(int(sys.stdin.readline().rstrip()))

max_value=float('-inf')

for i in range(N):
    if(tropy[i]>max_value):
        max_value=tropy[i]
        left+=1

max_value=float('-inf')

for i in range(N-1,-1,-1):
    if(tropy[i]>max_value):
        max_value=tropy[i]
        right+=1

print(left)
print(right)
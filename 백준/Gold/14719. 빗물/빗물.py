import sys

input=sys.stdin.readline

H,W=map(int,input().split())
building=list(map(int,input().split()))
answer=0

for i in range(1,len(building)):
    left_mv=max(building[:i])
    right_mv=max(building[i:])

    if(min(left_mv,right_mv)-building[i]>0):
        answer+=min(left_mv,right_mv)-building[i]
        
print(answer)
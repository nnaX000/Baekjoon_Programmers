import sys

N, D =map(int,sys.stdin.readline().strip().split(' '))

shortcut=[]
distance=[float('inf')]*(D+1)

for i in range(N):
    shortcut.append(list(map(int,sys.stdin.readline().strip().split(' '))))

distance[0]=0

shortcut.sort()

for i in range(D+1):
    if(i<D):
        distance[i+1]=min(distance[i+1],distance[i]+1)

    for start,end,cost in shortcut:
        if(start==i and end<=D):
            distance[end]=min(distance[end],distance[start]+cost)

print(distance[D])
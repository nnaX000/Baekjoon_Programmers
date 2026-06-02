n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
a_points=sorted(points,key=lambda x:x[1])
a_points=sorted(a_points,key=lambda x:x[0])

answer=0

cnt=float('inf')

for a,b in a_points:
    if(cnt!=a):
        answer+=b
        cnt=a

print(answer)
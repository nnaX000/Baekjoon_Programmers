import sys

tri={}

sum_value=0

for i in range(3):
    tmp=int(sys.stdin.readline().rstrip())
    if(tmp in tri):
        tri[tmp]+=1
        sum_value+=tmp
    else:
        tri[tmp]=1
        sum_value+=tmp

if(sum_value==180):
    if(len(tri)==1):
        print("Equilateral")
    elif(len(tri)==2):
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
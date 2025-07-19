import sys

X=int(sys.stdin.readline().rstrip())

stand=2
sum_value=1
row=0

while(True):
    if(sum_value>=X):
        stand-=1
        break
    sum_value+=(stand)
    stand+=1
    row+=1

ram=X-(sum_value-stand)

if(row%2==0):
    x=row
    y=0
    for i in range(ram-1):
        x-=1
        y+=1
else:
    x=0
    y=row
    for i in range(ram-1):
        x+=1
        y-=1

print(str(x+1)+"/"+str(y+1))
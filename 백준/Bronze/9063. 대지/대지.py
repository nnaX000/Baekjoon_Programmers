import sys

array=[]

x_max_value=-10001
x_min_value=10001
y_max_value=-10001
y_min_value=10001

N=int(sys.stdin.readline().rstrip())

for i in range(N):
    tmp=list(map(int,sys.stdin.readline().rstrip().split(' ')))
    array.append(tmp)

for i in array:
    if(i[0]>x_max_value):
        x_max_value=i[0]
    if(i[0]<x_min_value):
        x_min_value=i[0]

for i in array:
    if(i[1]>y_max_value):
        y_max_value=i[1]
    if(i[1]<y_min_value):
        y_min_value=i[1]

print(abs(x_max_value-x_min_value)*abs(y_max_value-y_min_value))
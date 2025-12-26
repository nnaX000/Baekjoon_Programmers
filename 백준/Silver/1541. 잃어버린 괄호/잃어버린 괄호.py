import sys

input=sys.stdin.readline

N=input()

array=[]
tmp=""

n_array=N.split('-')
result=0

for i in range(len(n_array)):
    tmp=n_array[i].split('+')
    sum_value=0

    for j in tmp:
        if(j!="+"):
            sum_value+=int(j)

    if(i==0):
        result+=sum_value
    else:
        result-=sum_value

print(result)
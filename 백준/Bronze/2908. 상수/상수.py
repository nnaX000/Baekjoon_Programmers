import sys

array=list(sys.stdin.readline().rstrip().split(' '))
new_array=[]

for i in array:
    tmp=""
    for j in reversed(i):
        tmp+=j
    new_array.append(tmp)

print(max(new_array))
import sys

tmp=int(sys.stdin.readline().rstrip())
sum_value=0
value=0

for i in range(1,tmp-1):
    value=value+i
    sum_value+=value

print(sum_value)
print(3)
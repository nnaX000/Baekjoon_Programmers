import sys

input=sys.stdin.readline

x,y=map(int,input().split())

day=["SUN","MON", "TUE", "WED", "THU", "FRI", "SAT"]

month=[0,31,28,31,30,31,30,31,31,30,31,30,31]

sum_value=0

for i in range(x):
    sum_value+=month[i]

sum_value+=y
sum_value%=7

print(day[sum_value])
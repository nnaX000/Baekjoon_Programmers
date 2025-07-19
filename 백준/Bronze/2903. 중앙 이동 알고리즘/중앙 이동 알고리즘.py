import sys

N=int(sys.stdin.readline().rstrip())

array=[2]
k=1

for i in range(15):
    array.append(array[-1]+k)
    k*=2

print(array[N]**2)
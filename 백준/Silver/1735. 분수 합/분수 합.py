import sys
import math

a_1,b_1=map(int,sys.stdin.readline().rstrip().split(' '))
a_2,b_2=map(int,sys.stdin.readline().rstrip().split(' '))

top=(a_1*b_2)+(b_1*a_2)
bottom=(b_1*b_2)

array=[]

gcd=math.gcd(top,bottom)

top//=gcd
bottom//=gcd

print(top,end=" ")
print(bottom)
import sys

a_1,b_1=map(int,sys.stdin.readline().rstrip().split(' '))
a_2,b_2=map(int,sys.stdin.readline().rstrip().split(' '))

top=(a_1*b_2)+(b_1*a_2)
bottom=(b_1*b_2)

for i in range(2,int(min(top,bottom)**1/2)+1):
    if(top%i==0 and bottom%i==0):
        while(top%i==0 and bottom%i==0):
            top//=i
            bottom//=i

print(top,end=" ")
print(bottom)
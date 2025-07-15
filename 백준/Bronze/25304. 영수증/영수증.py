X=int(input())
N=int(input())

sum_value=0

for i in range(N):
    price,amount=map(int,input().split(' '))
    sum_value+=price*amount

if(sum_value==X):
    print("Yes")
else:
    print("No")
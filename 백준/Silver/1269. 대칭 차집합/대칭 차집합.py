aNum,bNum=map(int,input().split(' '))
a=set(map(int,input().split(' ')))
b=set(map(int,input().split(' ')))
achab=a-b
bchaa=b-a
print(len(achab|bchaa))
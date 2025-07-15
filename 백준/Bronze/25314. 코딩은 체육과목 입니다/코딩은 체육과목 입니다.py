N=int(input())

for i in range((N//4)):
    print("long",end=" ")

if(N%4!=0):
    print("long",end=" ")

print("int")
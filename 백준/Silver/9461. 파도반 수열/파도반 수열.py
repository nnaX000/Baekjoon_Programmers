#1 1 1 2 2 3 4 5 7 9 12 16(+4) 21(+5) 28(+7) 37(+9) 49(+12)
#1 2 3 4 5 6 7 8 9 10
answer=[]
basic=[0]*1000
basic[0:5]=[1,1,1,2,2]
num=int(input())
for i in range(num):
    a=int(input())
    if(basic[a]!=0):
        answer.append(basic[a-1])
    else:
        for j in range(5,a):
            basic[j]=basic[j-1]+basic[j-5]
        answer.append(basic[a-1])
for i in answer:
    print(i)

import sys
from collections import defaultdict

input=sys.stdin.readline

r,c,k=map(int,input().split()) # A[r][c] = k

A=[list(map(int,input().split())) for _ in range(3)]

array=[[0 for _ in range(100)] for _ in range(100)]

for i in range(len(A)):
    for j in range(len(A[0])):
        array[i][j]=A[i][j]

count=0

if(array[r-1][c-1]==k):
    print(count)
    sys.exit(0)

c_num=3
r_num=3

while(count<100):

    if(r_num>=c_num): # 행개수가 열 개수보다 크거나 같은 경우 -> R 연산
        #print("R")
        mc_num=0

        for i in range(r_num):
            d=defaultdict(int)

            for j in range(c_num):
                d[array[i][j]]+=1

            if(0 in d):
                del d[0]

            # 값 기준 정렬
            d=dict(sorted(d.items()))

            # 값 기준 정렬
            d=dict(sorted(d.items(),key=lambda x:x[1]))

            num=0
            
            if(len(d)>50):
                mc_num=100
            else:
                mc_num=max(len(d)*2,mc_num)

            for key,value in d.items():
                array[i][num]=key
                if(num<100):
                    array[i][num+1]=value
                num+=2
                if(num==100):
                    break

            for t in range(num, 100):
                array[i][t] = 0

        c_num=mc_num

    else: # 행 개수가 열 개수보다 작은 경우 -> C 연산
        #print("C")
        mr_num=0

        for i in range(c_num):
            d=defaultdict(int)

            for j in range(r_num):
                d[array[j][i]]+=1

            if(0 in d):
                del d[0]

            # 키 기준 정렬
            d=dict(sorted(d.items()))

            # 값 기준 정렬
            d=dict(sorted(d.items(),key=lambda x:x[1]))

            if(len(d)>50):
                mr_num=100
            else:
                mr_num=max(len(d)*2,mr_num)

            num=0
            for key,value in d.items():
                array[num][i]=key
                if(num<100):
                    array[num+1][i]=value
                num+=2
                if(num==100):
                    break

            for t in range(num, 100): # 안 밀어줌.
                array[t][i] = 0

        r_num=mr_num
    
    count+=1

    if(array[r-1][c-1]==k):
        print(count)
        sys.exit(0)

print(-1)
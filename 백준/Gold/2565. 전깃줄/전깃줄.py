#[연결했을때,내려온 최댓값]
stack=[]
num=int(input())
dp=[[0,0] for i in range(num)]
array=[]
count=1
for i in range(num):
    temp=list(map(int,input().split(' ')))
    array.append(temp)
array=sorted(array,key=lambda x:x[0])
for j in range(num):
    if(j>0):
        max=0
        for i in range(len(dp)):
            if(dp[i][1]<array[j][1]):
                if(dp[i][0]>max):
                    max=dp[i][0]
        if(max!=0):
            dp[j][0]=max+1
            dp[j][1]=array[j][1]
            count+=1
        else:
            dp[j][0]=1
            dp[j][1]=array[j][1]
    else:
        dp[0][0]=1
        dp[0][1]=array[0][1]
answer=sorted(dp,key=lambda x:x[0])
if(answer[-1][0]!=num):
    print(num-answer[-1][0])
else:
    print(0)
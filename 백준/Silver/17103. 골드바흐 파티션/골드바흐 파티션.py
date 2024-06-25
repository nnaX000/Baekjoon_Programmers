#4부터 시작
#0 1 2 3
#4 6 8 10
import sys
num=int(sys.stdin.readline())
array=[]
result=[]
sample=[0 for i in range(1000001)]#0소수임 1 소수 아님 0~10000000
sample[0]=1
sample[1]=1
for idx,value in enumerate(sample):
    gap=1
    if(sample[idx]==0):
        for j in range(2*idx,len(sample),idx):
            sample[j]=1
for i in range(num):
    tmp=int(sys.stdin.readline())
    answer = 0
    for j in range(2, (tmp // 2) + 1, 1):
        if (j == 2 or j % 2 != 0):
            ram = tmp - j
            if (sample[j]==0 and sample[ram]==0):
                answer += 1
    result.append(answer)

for i in result:
    print(i)


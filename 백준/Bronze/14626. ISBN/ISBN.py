import sys

isbm=sys.stdin.readline().rstrip()
sum_value=0
num=1
star=1
check=int(isbm[-1])

for idx,i in enumerate(isbm):
    if(idx!=12):
        if(i!="*"):
            if(num==1):
                sum_value+=int(i)
                num=3
            else:
                sum_value+=(int(i)*3)
                num=1
        else:
            star=num
            num = 1 if num==3 else 3

for i in range(0,10):
    sum_value+=(star*i)

    if(((10-(sum_value%10))%10)==check):
        print(i)
        sys.exit(0)

    sum_value-=(star*i)
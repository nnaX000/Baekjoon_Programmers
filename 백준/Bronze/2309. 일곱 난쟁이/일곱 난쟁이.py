import sys

seven=[]

for i in range(9):
    seven.append(int(sys.stdin.readline().rstrip()))

sum_value=sum(seven)

out=sum_value-100

solve=False

for i in range(len(seven)-1):
    tmp=seven[i]
    for j in range(i+1,len(seven)):
        compare=seven[j]
        if(tmp+compare==out):
            seven.remove(tmp)
            seven.remove(compare)
            solve=True
            break
    if(solve):
        break

seven.sort()

for i in seven:
    print(i)
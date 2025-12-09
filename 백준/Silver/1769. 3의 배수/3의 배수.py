import sys

tmp=sys.stdin.readline().rstrip()
num=0

while(len(tmp)>1):
    tmp_1=0
    for i in tmp:
        tmp_1+=int(i)

    tmp=str(tmp_1)
    num+=1

print(num)
tmp=int(tmp)

if(tmp==3 or tmp==6 or tmp==9):
    print("YES")
else:
    print("NO")
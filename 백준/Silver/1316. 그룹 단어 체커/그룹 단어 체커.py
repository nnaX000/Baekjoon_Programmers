import sys
num=int(sys.stdin.readline())
answer=0
for i in range(num):
    group = True
    set = {0}
    stand="0"
    tmp=sys.stdin.readline()
    for i in tmp:
        if(i not in set):
            set.add(i)
            stand=i
        elif(stand!=i and i in set):
            group=False
            break

    if(group):
        answer+=1
print(answer)
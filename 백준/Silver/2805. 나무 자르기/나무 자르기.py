global dic
def BinarySearch(dic,a,x,y):
    middle=(y+x)//2
    total = sum([a[i] - middle for i in range(num) if a[i] > middle])
    if (total < goal):
        if (middle in dic):
            return dic
        else:
            dic[middle] = total
            return BinarySearch(dic, a, x, middle)
    elif (total > goal):
        if(middle in dic):
            return dic
        else:
            dic[middle]=total
            return BinarySearch(dic,a,middle,y)
    else:
        dic[middle]=total
        return dic

num,goal=input().split()
num=int(num)
goal=int(goal)
a=list(map(int,input().split()))
a.sort()
dic={}
if(num==1):
    print(a[0]-goal)
else:
    dic=BinarySearch(dic,a,1,a[-1])
    filtered_dict = {key: value for key, value in dic.items() if value >= goal}
    answer = sorted(filtered_dict.items(), key=lambda x: x[1])
    if (len(answer) >= 1):
        print(int(answer[0][0]))
    else:
        print(0)
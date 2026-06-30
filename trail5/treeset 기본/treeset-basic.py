from sortedcontainers import SortedSet

n = int(input())
s = SortedSet()

for _ in range(n):
    line = input().split()

    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        num=int(line[1])

        if(line[0]=="add"):
            s.add(num)
        elif(line[0]=="remove"):
            s.remove(num)
        elif(line[0]=="find"):
            if(num in s):
                print("true")
            else:
                print("false")
        elif(line[0]=="lower_bound"):
            tmp=s.bisect_left(num)

            if(tmp<len(s)):
                print(s[tmp])
            else:
                print("None")
        elif(line[0]=="upper_bound"):
            tmp=s.bisect_right(num)

            if(tmp<len(s)):
                print(s[tmp])
            else:
                print("None")
    else:
        if(line[0] == "largest"):
            if(s):
                print(s[-1])
            else:
                print("None")
        else:
            if(s):
                print(s[0])
            else:
                print("None")


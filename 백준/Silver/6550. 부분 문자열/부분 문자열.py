import sys

input=sys.stdin.readline

while(True):
    try:
        s,t=input().split()

        idx=0
        count=0

        for i in range(len(t)):
            if(s[idx]==t[i]):
                count+=1
                idx+=1

            if(count==len(s)):
                break

        if(count==len(s)):
            print("Yes")
        else:
            print("No")
            
    except:
        break
from collections import Counter

str = input()

# Please write your code here.
result=Counter(str)
check=False

for a,b in result.items():
    if(b==1):
        print(a)
        check=True
        break

if(not check):
    print("None")
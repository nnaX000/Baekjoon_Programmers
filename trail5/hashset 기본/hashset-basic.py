n = int(input())
commands = []

hashset=set()

for _ in range(n):
    cmd, val = input().split()
    val=int(val)

    if(cmd=="find"):
        if(val in hashset):
            print("true")
        else:
            print("false")
    elif(cmd=="remove"):
        hashset.remove(val)
    else:
        hashset.add(val)

# Please write your code here.

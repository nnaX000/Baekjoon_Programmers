from collections import defaultdict

n = int(input())

nums=defaultdict(int)

for _ in range(n):
    line = input().split()
    cmd=line[0]

    if line[0] == "add":
        k,v=int(line[1]),int(line[2])
        nums[k]=v
    elif line[0] == "remove":
        k=int(line[1])
        del nums[k]
    elif line[0] == "find":
        k=int(line[1])
        if(k in nums):
            print(nums[k])
        else:
            print("None")
    else:
        nums=dict(sorted(nums.items(), key=lambda x:x[0]))

        if(len(nums)>0):
            for k,v in nums.items():
                print(v,end=" ")
            print()
        else:
            print("None")

import sys

attend=[0]*31

for i in range(28):
    x=int(sys.stdin.readline().rstrip())
    attend[x]=1

for i in range(1,len(attend)):
    if(attend[i]==0):
        print(i)
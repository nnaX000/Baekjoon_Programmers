import sys

T=int(sys.stdin.readline().rstrip())

for i in range(T):
    tmp=sys.stdin.readline().rstrip()
    print(tmp[0],end="")
    print(tmp[-1])
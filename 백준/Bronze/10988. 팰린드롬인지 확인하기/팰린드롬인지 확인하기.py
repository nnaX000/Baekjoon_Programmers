import sys

tmp=sys.stdin.readline().rstrip()

tmp_reversed=tmp[::-1]

if(tmp==tmp_reversed):
    print(1)
else:
    print(0)
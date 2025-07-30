import sys

S=sys.stdin.readline().rstrip()

one_count=0
zero_count=0

answer=0

stand=""

for i in S:
    if(i=="0"):
        if(i!=stand):
            zero_count+=1
            stand="0"
    else:
        if(i!=stand):
            one_count+=1
            stand="1"

answer+=min(one_count,zero_count)

print(answer)
import sys

format=sys.stdin.readline().rstrip()

#c가 문자 위치하는 자리, d가 숫자 위치하는 자리

answer=1
stand=0

for i in range(len(format)):

    if(i>0):
        if(format[i-1]==format[i]):
            stand=1
        else:
            stand=0

    if(format[i]=="c"):
        answer*=(26-stand)
    else:
        answer*=(10-stand)

print(answer)
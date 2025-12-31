import sys

input=sys.stdin.readline

N,r,c=map(int,input().split()) # 3,5,1

answer=0

stand=2**N

while(stand>1):
    stand//=2

    r_value=r//stand 
    c_value=c//stand

    answer+=((stand**2)*2)*r_value # 위에 있는 무리 더해줌
    answer+=(stand**2)*c_value # 왼쪽에 있는 무리 더해줌

    r-=r_value*stand
    c-=c_value*stand

print(answer)
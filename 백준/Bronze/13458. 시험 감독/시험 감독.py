import sys

N=int(sys.stdin.readline().rstrip()) #시험장 개수

A_i=list(map(int,sys.stdin.readline().rstrip().split(' ')))#i번째 시험장에 있는 응시자 수

B,C=map(int,sys.stdin.readline().rstrip().split(' '))#총 감독관 감시 가능인원/부감독관

total_super=0

sub_super=0

for i in range(N):
    if(A_i[i]>=B):
        total_super+=1
        if((A_i[i]-B)%C!=0):
            sub_super+=((A_i[i]-B)//C)+1
        else:
            sub_super+=((A_i[i]-B)//C)
    else:
        total_super+=1

print(total_super+sub_super)
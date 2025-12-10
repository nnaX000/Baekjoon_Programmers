import sys

#높이만큼 주위를 비출 수 있다. 왼쪽으로 높이만큼, 오른쪽으로 높이만큼.
#최소한의 높이로 굴다리의 모든 길 0~N을 밝히고자 한다.
#높이는 다 같아야 한다.

N=int(sys.stdin.readline().rstrip()) # 굴다리 길이 : 0~N
M=int(sys.stdin.readline().rstrip()) # 가로등 개수
x=list(map(int,sys.stdin.readline().rstrip().split(' ')))
x.sort()

min_value=x[0]

for i in range(1,M):
    if((x[i]-x[i-1])%2==0):
        tmp=(x[i]-x[i-1])//2
    else:
        tmp=((x[i]-x[i-1])//2)+1

    min_value=max(min_value,tmp)

min_value=max(min_value,N-x[-1])

print(min_value)
import sys

N=int(sys.stdin.readline().rstrip())
B=list(map(int,sys.stdin.readline().rstrip().split(' ')))

min_value=float('inf')

if(N>=2):
    for b0 in [B[0] - 1, B[0], B[0] + 1]:
        for b1 in [B[1] - 1, B[1], B[1] + 1]:
            ok=True
            diff = b1 - b0
            count = 0

            if B[0] != b0:
                count += 1
            if B[1] != b1:
                count += 1

            for k in range(2,N):
                nxt=b0 + (diff*k)
                if(abs(B[k] - nxt) > 1):
                    ok=False
                    break
                elif(abs(B[k] - nxt) == 1):
                    count+=1

            if(ok):
                min_value = min(min_value,count)
else:
    min_value=0

if(min_value==float('inf')):
    print(-1)
else:
    print(min_value)
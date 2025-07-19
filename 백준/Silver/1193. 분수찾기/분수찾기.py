import sys

X=int(sys.stdin.readline().rstrip())

ax=0
ay=0
tmp=-1

if(X==1):
    ax=0
    ay=0
else:   
    for i in range(X-1):
        if(ax+tmp<0 or ay-tmp<0):
            if(tmp==-1):
                tmp=1
                ay+=1
            else:
                tmp=-1
                ax+=1
        else:
            ax+=tmp
            ay-=tmp


print(str(ax+1)+"/"+str(ay+1))
    
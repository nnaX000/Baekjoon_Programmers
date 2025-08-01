import sys

E,S,M=map(int,sys.stdin.readline().rstrip().split(' '))

year=1
E_O=1
S_O=1
M_O=1

while(True):
    if(E_O==E and S_O==S and M_O==M):
        print(year)
        break

    E_O=15 if E_O+1 == 15 else (E_O+1)%15
    S_O=28 if S_O+1 == 28 else (S_O+1)%28
    M_O=19 if M_O+1 == 19 else (M_O+1)%19
    
    year+=1
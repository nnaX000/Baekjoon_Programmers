while(True):
    try:
        tmp=input()
        a,b=tmp.split(' ')
        print(int(a)+int(b))
    except (ValueError, EOFError):
        break
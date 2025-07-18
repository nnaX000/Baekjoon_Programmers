import sys

here_x, here_y, w, h=map(int,sys.stdin.readline().rstrip().split(' '))

min_value=min(abs(0-here_y),abs(h-here_y),abs(here_x-0),abs(w-here_x))

print(min_value)

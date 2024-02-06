import sys
import math

def main():
    [ax, ay, bx, by] = list(map(int, sys.stdin.readline().strip("\n").split()))
    [cx, cy, dx, dy] = list(map(int, sys.stdin.readline().strip("\n").split()))

    x = max(ax,bx,cx,dx) - min(ax,bx,cx,dx)
    y = max(ay,by,cy,dy) - min(ay,by,cy,dy)

    print(max(x, y) ** 2)

main()
import sys

def main():

    sys.stdin = open("teleport.in", "r")
    sys.stdout = open("teleport.out", "w")

    [a, b, x, y] = list(map(int, sys.stdin.readline().strip("\n").split()))
    [a, b] = sorted([a, b])
    [x, y] = sorted([x, y])

    steps = min(b - a, abs(a-x) + abs(b - y))

    print(steps)

main()
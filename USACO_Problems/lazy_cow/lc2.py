import sys

def main():
    [n, k] = list(map(int, sys.stdin.readline().strip("\n").split()))
    location = [0] * 1000000

    for _ in range(n):
        [g, x] = list(map(int, sys.stdin.readline().strip("\n").split()))
        location[x] = g
        
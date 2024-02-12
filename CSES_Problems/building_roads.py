import sys

def main():
    [c, r] = list(map(int, sys.stdin.readline().strip().split()))
    a = []
    b = []
    for i in range(r):
        [A, B] = list(map(int, sys.stdin.readline().strip("\n").split()))
        a.append(A)
        b.append(B)

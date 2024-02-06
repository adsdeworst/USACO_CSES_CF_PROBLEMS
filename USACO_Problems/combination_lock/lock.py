# 49 50 1 2 3
# 50 1 2 3 4
# 1 2 3 4 5

# 3 4 5 6 7  1 overlap
# 4 5 6 7 8  1 overlap
# 5 6 7 8 9  1 overlap

# 3 - 1 2 3 4 5
# 4 - 2 3 4 5 6


import sys

def main():
    max = int(sys.stdin.readline().strip("\n"))
    fj_lock = list(map(int, sys.stdin.readline().strip("\n").split()))
    master_lock = list(map(int, sys.stdin.readline().strip("\n").split()))

    overlaps = 0

def diff(master_lock, fj_lock):
    for i in range(3):
        range = []
        for k in range(-2, 2, 1):
            range.append(master_lock[i] + k)

main()
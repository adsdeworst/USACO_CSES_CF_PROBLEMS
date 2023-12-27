import sys
import math

def main():
    hill_heights = []
    for _ in range(int(sys.stdin.readline().strip("\n"))):
        hill_heights.append(int(sys.stdin.readline().strip("\n")))

    min_cost = 100000000
    for i in range(max(hill_heights) - 17):
        cost = 0
        for k in hill_heights:
            if k > i + 17:
                cost += math.pow(k - (i + 17), 2)
            elif k < i:
                cost += math.pow(i - k, 2)
            else:
                continue

        if cost < min_cost:
            min_cost = cost
    
    print(int(min_cost))

main()
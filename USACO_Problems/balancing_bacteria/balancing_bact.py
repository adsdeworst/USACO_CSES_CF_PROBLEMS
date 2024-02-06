import sys
import math

def main():
    patches = int(input().strip("\n"))
    actions = []
    patch_status = list(map(int, input().strip("\n").split()))

    for i in range(patches):
        delta = 0
        for k in range(len(actions)):
            delta += actions[k] * (len(actions) + 1 - k)
        actions.append(-1 * (patch_status[i] + delta))

    sum = 0
    for i in actions:
        sum += abs(i)
    print(sum)

main()
import sys
from collections import Counter
half_numCows = 0
def main():
    for i in range(int(sys.stdin.readline().strip("\n"))):
        numCows = int(sys.stdin.readline().strip("\n"))
        preferences = list(map(int, sys.stdin.readline().strip("\n").split()))
        result = set()

        half_numCows = 3

        if numCows == 1:
            result.add(preferences[0])
        if numCows == 2:
            if preferences[0] == preferences[1]:
                result.add(preferences[0])
            else:
                result.add(-1)
        else:
            for i in range(numCows - half_numCows + 1):
                focus_group = preferences[i:i + half_numCows]
                # print(focus_group)
                result.add(get_greater_than_half(half_numCows, focus_group))
        
        result = sorted(list(result))
        if (-1 in result) and len(result) == 1:
            print(-1)
        else:
            print(" ".join(list(map(str, result))))

def get_greater_than_half(half_numCows, focus_group):
    counts = Counter(focus_group)
    for i in counts.keys():
        if counts[i] >= half_numCows//2 + 1:
            return i
    return -1


main()
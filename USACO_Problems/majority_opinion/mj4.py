import sys
from collections import Counter

def main():
    for _ in range(int(sys.stdin.readline().strip())):
        totalCattle = int(sys.stdin.readline().strip())
        choices = list(map(int, sys.stdin.readline().strip().split()))
        outcomes = []

        minimumRequired = 3  # Renamed from half_numCows for clarity

        if totalCattle == 1:
            outcomes.append(choices[0])
        elif totalCattle == 2:
            outcomes.append(choices[0] if choices[0] == choices[1] else -1)
        else:
            for j in range(totalCattle - minimumRequired + 1):
                sample = choices[j:j + minimumRequired]
                outcomes.append(find_majority(minimumRequired, sample))
        if len(outcomes) == 1 and outcomes[0] == -1:
            print(-1)
        else:
            outcomes = set(outcomes)
            outcomes = sorted(list(outcomes))
            print(" ".join(map(str, outcomes)))

def find_majority(minReq, sample):
    frequency = Counter(sample)
    for item in frequency:
        if frequency[item] >= (minReq // 2) + 1:
            return item
    return -1

main()

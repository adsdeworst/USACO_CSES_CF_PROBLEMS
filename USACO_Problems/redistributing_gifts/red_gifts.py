import sys

class Cow:
    def __init__(self, prefernces):
        self.preferences = prefernces
        neighbors = [[] for _ in range(n - 1)]

        for i in range(n - 1):
            neighbors[i].append(prefernces[i + 1])
        
        print(neighbors)

n = int(input())
cows = []
visited = [False for _ in range(n - 1)]
original = [i for i in range(1, n + 1)]
for _ in range(n):
    cows.append(Cow(list(map(int, input().split()))))
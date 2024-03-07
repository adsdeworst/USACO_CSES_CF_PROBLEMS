import sys

class Cow:
    def __init__(self, cow:int, prefernces:list):
        prefernces.insert(0,0)
        self.preferences = prefernces
        self.cow = cow


n = int(input())
cows = []
G = [[] for i in range(1 + n)]
for cow in range(1, n + 1):
    cows.append(Cow(cow, list(map(int, input().split()))))

for cow in cows:
    for pref in range(1, n + 1):
        if cow.preferences.index(cow.cow)>= pref and not (pref in G[cow.preferences[pref]]):
            G[cow.cow].append(pref)
    
print(G)
    
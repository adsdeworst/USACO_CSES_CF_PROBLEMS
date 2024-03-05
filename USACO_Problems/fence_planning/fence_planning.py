import sys

class Cow:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n, k = list(map(int, input().split()))
cows = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    cows.append(Cow(x, y))
    
neighbors = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for _ in range(k):
    a, b = list(map(int, input().split))
    neighbors[a].append(b)
    neighbors[b].append(a)


def dfs(node):
    answer = 0
    if not visited[node]:
        visited[node] = True
        for v in neighbors[node]:
            dfs(v)
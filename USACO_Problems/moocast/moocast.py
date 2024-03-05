from queue import Queue
import sys

sys.stdin = open("moocast.in", "r")
sys.stdout = open("moocast.out", "w")
class Cow:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p

n = int(input())
cows = []
for _ in range(n):
    (x, y, p) = list(map(int, input().split()))
    cows.append(Cow(x, y, p))

neighbors = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (cows[i].x - cows[j].x)**2 + (cows[i].y - cows[j].y)**2 <= cows[i].p**2:
            neighbors[i].append(j)

answer = 0
for start in range(n):
    visited = [False] * n
    # minDist = [0] * n
    q = Queue()
    q.put(start)
    reachableVertices = 1
    visited[start] = True
    # minDist[start] = 0
    while not q.empty():
        u = q.get() # this also removes the object
        for v in neighbors[u]:
        # Process the directed edge u->v:
            if not visited[v]:
                q.put(v)
                reachableVertices += 1
                visited[v] = True
            # minDist[v] = minDist[u] + 1
    answer = max(answer, reachableVertices)

print(answer)

import sys

sys.stdin = open("fenceplan.in", 'r')
sys.stdout = open("fenceplan.out", 'w')

sys.setrecursionlimit(10**8)

class Cow:
    def __init__(self, x, y):
        self.x = x
        self.y = y

n, k = list(map(int, input().split()))
cows = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    cows.append(Cow(x,  y))
    
neighbors = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for _ in range(k):
    a, b = list(map(int, input().split()))
    neighbors[a - 1].append(b - 1)
    neighbors[b - 1].append(a - 1)

LL = Cow(10**8, 10**8)
UR = Cow(-1, -1)
answer = 4*10**8
def dfs(node):
    global LL, UR
    if not visited[node]:
        visited[node] = True
        LL = Cow(min(LL.x, cows[node].x), min(LL.y, cows[node].y))
        UR = Cow(max(UR.x, cows[node].x), max(UR.y, cows[node].y))
        for v in neighbors[node]:
            dfs(v)
    # print(LL.x, LL.y, UR.x, UR.y)
    

def calcPerm(a:Cow, b:Cow):
    return (2 * abs(b.x - a.x) + 2 * abs(b.y - a.y))

for v in range(0, n):
    if not visited[v]:
        LL = Cow(cows[v].x, cows[v].y)
        UR = Cow(-1, -1)
        dfs(v)
        answer = min(answer, calcPerm(LL, UR))
    
print(answer)
import sys
from collections import deque
from queue import Queue

q = Queue([1, 2, 3])
print(q[0])


sys.setrecursionlimit(10 ** 6)

sys.stdin = open("closing.in", "r")
sys.stdout = open("closing.out", "w")

N, M = list(map(int, input().strip("\n").split()))
paths = [[] for _ in range(N)]
closing_order = []
for _ in range(M):
    a, b = list(map(int, input().split()))
    paths[a - 1].append(b - 1)
    paths[b - 1].append(a - 1)
for _ in range(N):
    closing_order.append(int(input().strip("\n")) - 1)
    
visited = [False] * N
closed = [False] * N

nodes = 0
def dfs(node):
    global nodes
    # q = deque(paths[node])
    q = paths[node]
    if not visited[node] and not closed[node]:
        visited[node] = True
        nodes += 1
        for elm in q:
            dfs(elm)
        
dfs(0)
if nodes == N:
    print("YES")
else:
    print("NO")
    
for i in range(N - 1):
    nodes = 0
    visited = [False] * N
    closed[closing_order[i]] = True
    dfs(closing_order[-1])    
    if nodes == N - i - 1:
        print("YES")
    else:
        print("NO")
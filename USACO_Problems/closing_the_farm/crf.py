"""
ID: advaith10
LANG: PYTHON3
TASK: 
"""

import sys
from collections import deque


sys.setrecursionlimit(10 ** 6)

# sys.stdin = open("closing.in", "r")
# sys.stdout = open("closing.out", "w")

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

def dfs(node):
    q = deque(paths[node])
    for i in q:
        if visited[i] == False and closed[i] == False:
            visited[i] = True
            dfs(i)
        
        
dfs(0)
if visited.count(True) == N:
    print("YES")
else:
    print("NO")
    
for i in range(N - 1):
    rep = []
    visited = [False] * N
    closed[closing_order[i]] = True
    for k in range(N):
        if visited[k] == True or closed[k] == True:
            continue
        rep.append(closing_order[-1])
        dfs(closing_order[-1])
    
    if len(rep) == 1:
        print("YES")
    else:
        print("NO")
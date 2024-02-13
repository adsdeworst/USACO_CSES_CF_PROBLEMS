"""
ID: advaith10
LANG: PYTHON3
TASK: 
"""

import sys
from collections import deque

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
        if visited[i] == False or closed[i] == False:
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

# import sys
# from collections import deque

# # sys.stdin = open("closing.in", "r")
# # sys.stdout = open("closing.out", "w")

# n, m = map(int, input().split())
# roads = []
# closing_order = []
# for _ in range(m):
#     roads.append(list(map(int, input().strip("\n").split())))
# for _ in range(n):
#     closing_order.append(int(input().strip("\n")) - 1)

# def dfs(node, not_inc):
#     q = deque(connected_barns[node])
#     for i in q:
#         if visited[i] and i in not_inc:
#             continue
        
#         visited[i] = True
#         dfs(i, not_inc)
# for l in range(n):
#     connected_barns = [[] for _ in range(n)]
#     closed_barns = []
#     rep_barns = []
#     visited = [False] * n
#     for k in closed_barns:
#         visited[k] = True
#     for i in range(m):
#         a, b = roads[i]
#         connected_barns[a - 1].append(b - 1)
#         connected_barns[b - 1].append(a - 1)
            
#     for i in range(len(closing_order)): 
#         if visited[i]:
#             continue

#         visited[i] = True
#         rep_barns.append(i)
#         dfs(i, closed_barns)
        
#     closed_barns.append(closing_order[0])
#     closing_order.pop(0)   
#     if len(rep_barns) > 2:
#         print("NO")
#     else:
#         print("YES")
    
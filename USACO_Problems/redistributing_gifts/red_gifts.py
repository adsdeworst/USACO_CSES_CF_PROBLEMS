import sys

class Cow:
    def __init__(self, cow:int, preferences:list):
        self.cow = cow
        self.preferences = preferences[:preferences.index(self.cow) + 1]


n = int(input())

cows = []
for cow in range(1, n + 1):
    cows.append(Cow(cow, list(map(int, input().split()))))
# print(cows)

G = [[] for i in range(1 + n)]
for cow in cows:
    G[cow.cow] = cow.preferences
# print(G)

isPath = [[False] * (1 + n) for _ in range(1 + n)]
for i in range(1, 1 + n):
    for j in G[i]:
        isPath[i][j] = True

# Transitive clojure.
for k in range(1, 1 + n): # The mid-point is the outermost for loop
    for i in range(1, 1 + n):
        for j in range(1, 1 + n):
            if(isPath[i][k] and isPath[k][j]):
                isPath[i][j] = True

answer = [0] * (1 + n)
for cow in cows:
    c = cow.cow
    for p in cow.preferences:
        if isPath[p][c]: # This cycle exists: c->p->...->c
            # Cow c can hope for the gift p.
            answer[c] = p
            break

for i in range(1, 1 + n):
    print(answer[i])


# import sys

# class Cow:
#     def __init__(self, cow:int, preferences:list):
#         self.cow = cow
#         self.preferences = preferences[:preferences.index(self.cow)]
#         self.preferences.append(self.cow)


# n = int(input())
# cows = []
# G = [[] for i in range(1 + n)]
# switched = [False] * (1 + n)
# reached = [0] * (1 + n)
# answer = []
# for cow in range(1, n + 1):
#     cows.append(Cow(cow, list(map(int, input().split()))))

# print(cows)


# for cow in cows:
#     for pref in cow.preferences:
#         G[cow.cow].append(pref)
    
# print(G)

# def dfs(node):
#     for elm in G[node]:
#         if node == elm:
#             reached[node] = elm
#             switched[node] = True
#         elif not switched[node]:
            

# dfs(1)
# dfs(2)
# dfs(3)
# dfs(4)
# print(reached)

# """
# 1 - 4
# 4 - 6
# 6 - 8
# 8 - 1
# 3 - 3
# 5 - 5
# 2 - 7
# 7 - 2
# """
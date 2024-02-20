from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

def main():
    cities, roads = list(map(int, input().strip("\n").split()))
    visited = [False] * cities
    connected_cities = [[] for _ in range(cities)]
    
    for _ in range(roads):
        a, b = list(map(int, input().strip("\n").split()))
        connected_cities[a - 1].append(b - 1)
        connected_cities[b - 1].append(a - 1)
    
    def dfs(node):
        q = deque(connected_cities[node])
        for i in q:
            if not visited[i]:
                visited[i] = True
                dfs(i)
    
    connected_comps = []
    for i in range(cities):
        if visited[i]:
            continue
        
        visited[i] = True
        connected_comps.append(i)
        dfs(i)
    
    print(len(connected_comps) - 1)
    for i in range(len(connected_comps) - 1):
        print(connected_comps[i] + 1, connected_comps[i + 1] + 1)
        
main()
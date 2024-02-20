from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n)]
for _ in range(m):
	a, b = map(int, input().split())
	adj[a - 1].append(b - 1)
	adj[b - 1].append(a - 1)


def dfs(node: int) -> None:
	for n in adj[node]:
		if not visited[n]:
			visited[n] = True
			dfs(n)


visited = [False for _ in range(n)]
rep_cities = []
for i in range(n):
	if visited[i]:
		continue

	visited[i] = True
	rep_cities.append(i)
	dfs(i)

print(len(rep_cities) - 1)
for i in range(len(rep_cities) - 1):
	print(rep_cities[i] + 1, rep_cities[i + 1] + 1)
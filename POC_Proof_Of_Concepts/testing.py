import sys

sys.stdin = open("closing.in", "r")
sys.stdout = open("closing.out", "w")

n, m = map(int, input().split())

adj, order = {}, []
for i in range(1, n + 1):
	adj[i] = []

visited, closed = [False] * (n + 1), [False] * (n + 1)
nodes = 0


def dfs(node):
	global nodes
	if visited[node] or closed[node]:
		return

	# Visit this node if it isn't closed and we haven't visited it yet.
	nodes += 1
	visited[node] = True

	for u in adj[node]:
		if not visited[u]:
			dfs(u)


# Read in adjacency list.
for i in range(m):
	a, b = map(int, input().split())
	adj[a].append(b)
	adj[b].append(a)

for i in range(n):
	order.append(int(input()))

dfs(1)

"""
The farm is initially connected if we've visited every node
before any of the farms are closed.
"""
print("YES") if nodes == n else print("NO")

for i in range(n - 1):
	visited = [False] * (n + 1)
	nodes = 0
	closed[order[i]] = True

	# Start DFS from the barn that will close last.
	dfs(order[n - 1])

	# Have we visited all the unclosed barns?
	if nodes == n - i - 1:
		print("YES")
	else:
		print("NO")
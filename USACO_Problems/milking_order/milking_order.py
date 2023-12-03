import sys

sys.stdin = open("USACO_Problems\\milking_order\\milking.in", "r")
sys.stdout = open("USACO_Problems\\milking_order\\milking.out", "w")

n, m, k = map(int, input().split())

hierarchy = [i - 1 for i in list(map(int, input().split()))]
order = [-1] * n

for i in range(k):
	cow, pos = map(int, input().split())

	order[pos - 1] = cow - 1

	if cow == 1:  # already fixed, nothing we can do
		print(pos)
		exit()


def check():
	"""
	:return whether it's possible to construct a
	valid ordering with given fixed elements
	"""
	new_order = order.copy()

	cow_to_pos = [-1] * n
	for i in range(n):
		if order[i] != -1:
			cow_to_pos[order[i]] = i

	h_idx = 0
	i = 0
	while i < n and h_idx < m:
		# we know the next cow has to be in front of it
		if cow_to_pos[hierarchy[h_idx]] != -1:
			if i > cow_to_pos[hierarchy[h_idx]]:
				return False

			i = cow_to_pos[hierarchy[h_idx]]
			h_idx += 1
		else:
			while i < n and new_order[i] != -1:
				i += 1

			# run out of places
			if i == n:
				return False

			new_order[i] = hierarchy[h_idx]
			cow_to_pos[hierarchy[h_idx]] = i
			h_idx += 1

		i += 1

	return True


for i in range(n):
	# if already fixed, skip
	if order[i] == -1:
		# try placing cow 1 @ position i
		order[i] = 0

		if check():
			print(i + 1)
			break

		order[i] = -1
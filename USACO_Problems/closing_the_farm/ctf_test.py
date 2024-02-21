import sys

a, b = list(map(int, input().strip("\n").split()))
order = []
for _ in range(b):
    order.append(list(map(int, input().strip("\n").split())))
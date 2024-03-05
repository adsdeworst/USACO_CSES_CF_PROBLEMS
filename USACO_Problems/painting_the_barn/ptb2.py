import sys

sys.stdin = open("paintbarn.in", "r")
sys.stdout = open("paintbarn.out", "w")


MAX_XY = 1000 + 1

delta = []
plane = []
for _ in range(MAX_XY):
  delta.append([0] * MAX_XY)
  plane.append([0] * MAX_XY)

(n, k) = list(map(int, input().split()))
for _ in range(n):
  (x1, y1, x2, y2) = list(map(int, input().split()))
  delta[x1][y1] += +1
  delta[x2][y1] += -1
  delta[x1][y2] += -1
  delta[x2][y2] += +1

plane[0][0] = delta[0][0]
for y in range(1, MAX_XY):
  plane[0][y] = delta[0][y] + plane[0][y - 1]
for x in range(1, MAX_XY):
  plane[x][0] = delta[x][0] \
              + plane[x - 1][0]
  for y in range(1, MAX_XY):
    plane[x][y] = delta[x][y] \
                + plane[x - 1][y] \
                + plane[x][y - 1] \
                - plane[x - 1][y - 1] \

answer = 0
for x in range(MAX_XY):
  for y in range(MAX_XY):
    # print(plane[x][y], end=" ")
    if plane[x][y] == k:
      answer += 1
  # print()

print(answer)

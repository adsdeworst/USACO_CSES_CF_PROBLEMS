import sys

def main():
  T = int(sys.stdin.readline())
  for _ in range(T):
    [N, K] = list(map(int, sys.stdin.readline().strip("\n").split()))
    cows = sys.stdin.readline().strip("\n")
    patches = 0
    grass = ["."] * N
    prev_h = -(K + 1)
    prev_g = -(K + 1)
    for i in range(N):
      cow = cows[i]
      if cow == 'H':
        if abs(i - prev_h) > K:
          prev_h = min(i + K, N - 1)
          if grass[prev_h] != ".":
            prev_h -= 1
          grass[prev_h] = 'H'
          patches += 1
      else:
        if abs(i - prev_g) > K:
          prev_g = min(i + K, N - 1)
          if grass[prev_g] != ".":
            prev_g -= 1
          grass[prev_g] = 'G'
          patches += 1
    print(patches)
    answer = ""
    for g in grass:
      answer += g
    print(answer)

main()

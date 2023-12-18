import sys

def main():
    [a, b] = list(map(int, sys.stdin.readline().strip("\n").split()))
    [c, d] = list(map(int, sys.stdin.readline().strip("\n").split()))

    fences = [0] * 100
    count = 0

    for i in range(a, b, 1):
      fences[i] = 1

    for j in range(c, d, 1):
        fences[j] = 1

    for k in fences:
       if k == 1:
          count += 1

    sys.stdout.write(str(count))
main()
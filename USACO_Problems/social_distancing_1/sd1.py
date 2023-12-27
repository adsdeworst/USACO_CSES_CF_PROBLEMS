import sys

def main():
    n = int(sys.stdin.readline().strip("\n"))
    stalls = sys.stdin.readline().strip("\n")

    empty_stalls = []

    count = 0
    for i in range(n):
        if count > 0 and stalls[i] == "0":
            empty_stalls.append(count)
        elif stalls[i] == "1":
            count += 1

        
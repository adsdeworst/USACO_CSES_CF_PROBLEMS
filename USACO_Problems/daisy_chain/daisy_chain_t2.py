import sys

def main():
    n = int(sys.stdin.readline().strip("\n"))
    num_list = list(map(int, sys.stdin.readline().strip("\n").split()))

    avg_flowers = 0

    for i in range(n):
        for k in range(i, n):
            if sum(num_list[i:k + 1])/(k - i + 1) in num_list[i:k + 1]:
                avg_flowers += 1

    print(avg_flowers)

main()
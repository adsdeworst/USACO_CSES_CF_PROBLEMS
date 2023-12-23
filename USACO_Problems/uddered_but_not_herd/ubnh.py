import sys

def main():
    order= sys.stdin.readline().strip("\n")
    word = sys.stdin.readline().strip("\n")

    count = 1
    for i in range(0, len(word) - 1, 1):
        if order.index(word[i]) >= order.index(word[i+1]):
            count += 1

    print(count)

main()
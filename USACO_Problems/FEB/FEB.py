import sys

def main():
    n = int(sys.stdin.readline().strip("\n"))
    conv = sys.stdin.readline().strip("\n")

    minimum = 0
    maximum = 0

    count = 0
    start = -1
    end = -1
    for i in range(n):
        if i == 0 and conv[i] == "F":
            maximum = 1
            minimum = 0
            count = -1

        if i > 0:
            if conv[i - 1] != "F" and conv[i] == "F":
                start = conv[i - 1]
        
        if conv[i] == "F":
            count += 1
            continue

        if count > 0 and conv[i] != "F":
            end = conv[i]
            if end == start:
                if count % 2 == 1:
                    minimum += 0
                    maximum += count + 1
                else:
                    minimum += 1
                    maximum += count + 1
            else:
                if count % 2 == 1:
                    minimum += 1
                    maximum += count
                else:
                    minimum += 0
                    maximum += count
            count = 0
        elif count > 0 and i == n - 1:
            minimum += 0

    print(minimum, maximum)

main()
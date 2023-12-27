import sys

def main():
    [d, h, m] = list(map(int, sys.stdin.readline().strip("\n").split()))
    days = d - 11
    hours = h - 11
    minutes = m - 11

    if hours < 0:
        days -= 1
        hours += 24

    if minutes < 0:
        hours -= 1
        minutes += 60

    print(days * 60 * 24 + hours * 60 + minutes)

main()
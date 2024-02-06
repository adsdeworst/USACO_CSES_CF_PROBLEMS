import sys

def main():
    fin = sys.stdin
    number = int(fin.readline().strip("\n"))
    met_nums = []
    pointer = -1

    while str(number)[pointer] not in met_nums:
        
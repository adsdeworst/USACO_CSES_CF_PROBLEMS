import sys

def main():
    [r, c] = list(map(int, sys.stdin.readline().strip("\n").split()))
    puddle_loc = []

    for i in range(r):
        line = sys.stdin.readline().strip("\n")
        line_list = []
        for k in line:
            line_list.append(k)
        puddle_loc.append(line_list)

    count = 0

    for line in range(r):
        for column in range(c):
            if puddle_loc[line][column] == "#":
                count += 1
                if column + 1 != c and line + 1 != r:
                    if puddle_loc[line][column + 1] == "#":
                        puddle_loc[line][column + 1] = "."
                    elif puddle_loc[line + 1][column] == "#":
                        puddle_loc[line + 1][column] = "."
                elif column + 1 == c and line + 1 != r:
                        puddle_loc[line + 1][column] = "."
                elif line + 1 == r and column + 1 != c:
                    puddle_loc[line][column + 1] = "."

    print(count)

main()
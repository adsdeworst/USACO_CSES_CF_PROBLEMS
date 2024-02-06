import sys

def main():
    grid = []

    for i in range(10):
        grid.append(sys.stdin.readline().strip("\n"))
        for k in range(10):
            if grid[i][k] == "B":
                barn = (k + 1, i + 1)
            elif grid[i][k] == "L":
                lake = (k + 1, i + 1)
            elif grid[i][k] == "R":
                rock = (k + 1, i + 1)

    steps = abs(barn[0] - lake[0]) + abs(barn[1] - lake[1])
    if barn[0] == rock[0] == lake[0] and (lake[1] > rock[1] > barn[1] or lake[1] < rock[1] < barn[1]):
        steps += 2
    elif barn[1] == rock[1] == lake[1] and (lake[0] > rock[0] > barn[0] or lake[0] < rock[0] < barn[0]):
        steps += 2

    print(steps - 1)
    
main()
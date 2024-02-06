import sys

def main():
    n = int(sys.stdin.readline().strip("\n"))
    checkpoints = []
    total_distance = 0
    min = 1000000000

    for _ in range(0, n):
        curr = list(map(int, sys.stdin.readline().strip("\n").split()))
        checkpoints.append(curr)

    for i in range(0, n - 1):
        total_distance += vertical_distance(checkpoints[i], checkpoints[i + 1])

    for i in range(1, n - 1):
        before = checkpoints[i - 1]
        current = checkpoints[i]
        after = checkpoints[i + 1]
        
        removed_distance = vertical_distance(before, current) + vertical_distance(current, after)
        added_distance = vertical_distance(before, after)

        if total_distance - removed_distance + added_distance < min:
            min = total_distance - removed_distance + added_distance
    
    print(min)
    return


def vertical_distance(point_1, point_2):
    return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

main()
import sys

def main():
    [number_line_length, curr_pos] = sys.stdin.readline().strip("\n").split()   
    targets = []
    values = []
    curr_pos = int(curr_pos)
    number_line_length = int(number_line_length)
    num_of_targets = 0
    for i in range(number_line_length):
        [curr_target, curr_value] = sys.stdin.readline().strip("\n").split()
        targets.append(int(curr_target))
        values.append(int(curr_value))
        if curr_target == "1":
            num_of_targets += 1

    delta = 1
    broken_targets = 0
    while curr_pos >= 0 and curr_pos < number_line_length and broken_targets < num_of_targets:
        if targets[curr_pos] == 1:
            if abs(delta) >= values[curr_pos]:
                targets[curr_pos] = -1
                broken_targets += 1
        elif targets[curr_pos] == 0:
            if delta < 0:
                delta = abs(delta) + targets[curr_pos]
            else:
                delta = -1 * (abs(delta) + targets[curr_pos])
        curr_pos += delta

    print(broken_targets)

main()
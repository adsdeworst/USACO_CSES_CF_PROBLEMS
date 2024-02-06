import sys

def main():
    [length, curr_pos] = list(map(int, sys.stdin.readline().strip("\n").split()))
    targets = []
    values = []
    curr_pos -= 1
    num_targets = 0
    for _ in range(length):
        [target, value] = list(map(int, sys.stdin.readline().strip("\n").split()))
        if target == 1:
            targets.append(1)
            num_targets += 1
        else:
            targets.append(0)
        values.append(value)


    delta = 1 # power = |move|
    targets_broken = 0
    while curr_pos >= 0 and curr_pos < length and targets_broken < num_targets:
        if targets[int(curr_pos)] == 1: # target
            if abs(delta) >= values[int(curr_pos)]:
                if targets[int(curr_pos)] != -1:
                    targets[int(curr_pos)] = -1 # target is broken
                    targets_broken += 1
        elif targets[int(curr_pos)] == 0:
            delta = - delta + (-1) * (delta/(abs(delta))) * values[int(curr_pos)]
            # if delta < 0:
            #     delta = - delta + values[curr_pos]
            #     # delta negative values pos
            #     # delta/abs(delta) * -1
            # else:
            #     delta = - delta - values[curr_pos]
            #     # delta positive values negative
        curr_pos += delta

    print(targets_broken)
    return

main()
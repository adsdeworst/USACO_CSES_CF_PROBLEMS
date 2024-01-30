import sys



def main():
    [length, pos] = list(map(int, sys.stdin.readline().strip("\n").split()))
    actions = []
    pos -= 1
    for i in range(length):
        actions.append(list(map(int, sys.stdin.readline().strip("\n").split())))

    move = 1 # power = |move|
    count = 0
    while pos > 0 and pos < length:
        [type_step, value] = actions[pos]
        if type_step == 1: # target
            if abs(move) >= value and value != 0:
                actions[pos][1] = 0
                count += 1
        elif type_step == 0:
            move = -1 * (abs(move) + value)
        pos += move

    print(count)

main()
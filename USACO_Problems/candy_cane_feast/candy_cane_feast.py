import sys

def main():
    input = sys.stdin
    output = sys.stdout

    [n, m] = list(map(int, input.readline().strip("\n").split()))
    cows_heights = list(map(int, input.readline().strip("\n").split()))
    cane_heights = list(map(int, input.readline().strip("\n").split()))

    for i in range(0, n - 1, 1):
        if cows_heights[i] > cows_heights[i+1]:
            cows_heights.pop(i+1)

    for i in range(m):
        candy_cane = [0, cane_heights[i]]
        for j in range(0, n - 1, 1):
            if cows_heights[i] < cows_heights[i+1]:
                if candy_cane[0] != candy_cane[1]:
                    candy_cane, cows_heights[j] = eat_candy_cane(candy_cane, cows_heights[j])
                else:
                    break
            else:
                continue

    for k in cows_heights:
        print(k)


def eat_candy_cane(candy_cane, cow_height):
    if candy_cane[1] > cow_height > candy_cane[0]:
        return [cow_height, candy_cane[1]], cow_height + (cow_height - candy_cane[0])
    elif cow_height < candy_cane[0]:
        return candy_cane, cow_height
    else: # cow_height > candy_cane[1]
        return [candy_cane[1], candy_cane[1]], cow_height + candy_cane[1]
    
main()
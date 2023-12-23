import sys

def main():
    sys.stdin = open("outofplace.in", 'r')
    sys.stdout = open("outofplace.out", 'w')

    n = int(sys.stdin.readline().strip("\n"))
    cow_locations = []
    swaps = 0

    for i in range(n):
        cow_locations.append(int(sys.stdin.readline().strip("\n")))

    for i in range(n - 2, -1, -1):
        if cow_locations[i] > cow_locations[i+1]: 
            if cow_locations[i-1] == cow_locations[i]:
                swaps += 0
            else:
                swaps += 1
                
            swap_val = cow_locations[i]
            cow_locations[i] = cow_locations[i+1]
            cow_locations[i+1] = swap_val

    print(str(swaps))
    return swaps

main()
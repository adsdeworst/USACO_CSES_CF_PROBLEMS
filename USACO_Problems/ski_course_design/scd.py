import sys

def main():
    hill_heights = []
    for _ in range(int(sys.stdin.readline().strip("\n"))):
        hill_heights.append(int(sys.stdin.readline().strip("\n")))
    hill_heights = sorted(hill_heights)
    print(hill_heights)

    print(make_less(hill_heights=hill_heights, sum=0))

def make_less(hill_heights, sum):
    if hill_heights[-1] - hill_heights[0] <= 17:
        return sum
    else:
        difference = hill_heights[-1] - hill_heights[0] - 17
        hill_heights[0] = hill_heights[0] + difference//2
        sum += (difference//2)**2
        difference = difference - difference//2
        hill_heights[-1] = hill_heights[-1] - difference
        sum += difference**2
        difference = difference - difference
        print(hill_heights)
        return make_less(sorted(hill_heights), sum)
    
main()
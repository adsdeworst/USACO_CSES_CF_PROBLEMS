# working sol

import sys

def main():
    input = sys.stdin
    output = sys.stdout

    [n, m] = list(map(int, input.readline().strip("\n").split()))
    cows_heights = list(map(int, input.readline().strip("\n").split()))
    cane_heights = list(map(int, input.readline().strip("\n").split()))

    for cane_height in range(m):
        lower_bound = 0
        # for cow_height in range(n):
        #     if max < cows_heights[cow_height]:
        #         max = cows_heights[cow_height]
        #         cows_heights[cow_height] = eats_candy_cane(cane_heights[cane_height], cows_heights[cow_height])
        for cow_height in range(n):
            diff = 0
            if cows_heights[cow_height] > lower_bound and cows_heights[cow_height] < cane_heights[cane_height]:
                diff = cows_heights[cow_height] - lower_bound
            elif cows_heights[cow_height] > lower_bound and cows_heights[cow_height] >= cane_heights[cane_height]:
                diff = cane_heights[cane_height] - lower_bound

            cows_heights[cow_height] += diff
            lower_bound += diff

            if lower_bound >= cane_heights[cane_height]:
                    break
    
    for i in cows_heights:
        print(i)

# def eats_candy_cane(cane_height, cow_height):
#     if cow_height < cane_height:
#         return cow_height + (cane_height - cow_height)
#     elif cow_height > cane_height:
#         return cow_height + cane_height
#     else:
#         return cow_height
    
main()
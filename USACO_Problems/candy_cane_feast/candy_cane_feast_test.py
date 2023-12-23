def feed_cows(N, M, cow_heights, candy_canes):
    cow_heights.sort(reverse=True)
    candy_canes.sort()

    result = []
    current_cane = 0

    for cow_height in cow_heights:
        while current_cane < M and candy_canes[current_cane] <= cow_height:
            cow_height += candy_canes[current_cane]
            current_cane += 1

        result.append(cow_height)

    return result


if __name__ == "__main__":
    # Read input
    N, M = map(int, input().split())
    cow_heights = list(map(int, input().split()))
    candy_canes = list(map(int, input().split()))

    # Get the result
    final_heights = feed_cows(N, M, cow_heights, candy_canes)

    # Print the result
    for height in final_heights:
        print(height)

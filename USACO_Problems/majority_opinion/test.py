for _ in range(int(input().strip())):
    cows = int(input().strip())
    hays = list(map(int, input().strip().split()))
    unique_results = set()

    if cows > 1 and hays[0] == hays[1]:
        unique_results.add(hays[0])

    for i in range(1, cows - 1):
        if hays[i] == hays[i - 1] or hays[i] == hays[i + 1]:
            unique_results.add(hays[i])
        elif hays[i - 1] == hays[i + 1]:
            unique_results.add(hays[i - 1])

    if cows > 1 and hays[-1] == hays[-2]:
        unique_results.add(hays[-1])

    result = sorted(unique_results) if unique_results else [-1]

    print(" ".join(map(str, result)))

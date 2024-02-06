import collections

for _ in range(int(input().strip("\n"))):
    cows = int(input().strip("\n"))
    hays = list(map(int, input().strip("\n").split()))
    result = set()

    for i in range(1, cows - 1):
        if hays[i-1] == hays[i] or hays[i] == hays[i + 1]:
            result.add(hays[i])
        elif hays[i - 1] == hays[i + 1]:
            result.add(hays[i - 1])
    
    result = sorted(list(result))
    if len(result) == 0:
        result.append(-1)

    print(" ".join(map(str, result)))

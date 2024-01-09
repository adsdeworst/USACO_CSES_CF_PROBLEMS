import sys

def main():
    test_cases = int(sys.stdin.readline().strip("\n"))
    for _ in range(test_cases):
        [n, k] = list(map(int, sys.stdin.readline().strip("\n").split()))
        string = sys.stdin.readline().strip("\n")
        count, result = get_result(n, k, string)
        print(str(count) + "\n" + string)


def get_result(n, k, places):
    result = ["."]*n
    count = 0
    for i in range(n):
        min_place = i - k
        max_place = i + k
        if i - k - 1 < 0: min_place = 0
        if i + k - 1 > n: max_place = n

        if not(places[i] in result[min_place:max_place]):
            if result[i + k - 1] != ".":
                count += 1
                result[i + k - 2] = places[i]
            else:
                count += 1
                result[i + k - 1] = places[i]
    
    return count, combine(result)

def combine(list):
    string = ""
    for i in list:
        string += str(i)

    return string

main()
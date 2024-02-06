import sys


def analyze_patterns(cows, stack):
    findings = set()

    if cows == 2:
        if stack[0] == stack[1]:
            return [stack[0]]
        else:
            return [-1]

    for index in range(1, cows - 1):
        if stack[index - 1] == stack[index] or stack[index] == stack[index + 1]:
            findings.add(stack[index])
        elif stack[index - 1] == stack[index + 1]:
            findings.add(stack[index - 1])
    
    return sorted(findings) if findings else [-1]

def main():
    for _ in range(int(sys.stdin.readline().strip("\n"))):
        herd_size = int(input().strip())
        feed_values = list(map(int, sys.stdin.readline().strip("\n").split()))

        analysis_result = analyze_patterns(herd_size, feed_values)

        print(" ".join(map(str, analysis_result)))


main()


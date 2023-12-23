import sys

def main():
    input = sys.stdin
    output = sys.stdout

    n = int(input.readline())
    infected_cow_list = list(map(int, [*input.readline().strip("\n")]))
    list_a = []
    one_counts = []
    count = 1

    section = infected_cow_list.index(1)
    for i in range(n):
        if i + 1 < n:
            if infected_cow_list[i] == 1 and infected_cow_list[i+1] == 0:
                list_a.append(infected_cow_list[section:i+1])
                section = i + 2
        else:
            if infected_cow_list[-1] == 1:
                list_a.append(infected_cow_list[section:])

    for i in list_a:
        one_counts.append(len(i))

    minimum = min(one_counts)
    days = minimum//2

    sum = 0
    if minimum % 2 == 1:
        days = (minimum-1)/2
        for i in one_counts:
            sum += len(i) - (2 * days)
    else:
        days = (minimum)/2
        for i in one_counts:
            sum += i - (2 * days)
    
    print(sum)

main()
import sys

def main():
    input = sys.stdin
    output = sys.stdout

    n = int(input.readline())
    infected_cow_list = list(map(int, [*input.readline().strip("\n")]))
    count = 1

    if infected_cow_list[-2] == 0 and infected_cow_list[-1] == 1:
        count = infected_cow_list.count(1)
    elif infected_cow_list[0] == 1 and infected_cow_list[1] == 0:
        count = infected_cow_list.count(1)
    elif infected_cow_list[-3] == 0 and infected_cow_list[-2] == 1 and infected_cow_list[-1] == 1:
        count = infected_cow_list.count(1)
    elif infected_cow_list[0] == 1 and infected_cow_list[1] == 1 and infected_cow_list[2] == 0:
        count = infected_cow_list.count(1)
    else:
        # if infected_cow_list[0] == infected_cow_list[-1] == 1:
        #     check_one = 1
        #     check_two = 0
        # elif infected_cow_list[0] == infected_cow_list[-1] == 1
        section = 0
        for i in range(0, n - 1, 1):
            if infected_cow_list[i-1] == 0 and infected_cow_list[i] == 1 and infected_cow_list[i+1] == 0:
                count = infected_cow_list.count(1)
                break
            elif infected_cow_list [i-2] == 0 and infected_cow_list[i-1] == 1 and infected_cow_list[i] == 1 and infected_cow_list[i+1] == 0:
                count = infected_cow_list.count(1)
                break
            # elif infected_cow_list[i] == check_one and infected_cow_list[i+1] == check_two:
            #     count += 1
            if infected_cow_list[i] == 1 and infected_cow_list[i+1] == 0:
                if infected_cow_list[section:i+1].count(1) % 2 == 1:
                    count += 1
                else:
                    count += 2
                section = i + 1

    print(count)

main()

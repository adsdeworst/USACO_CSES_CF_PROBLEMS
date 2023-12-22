import sys

def main():
    input = sys.stdin
    output = sys.stdout

    n = int(input.readline())
    infected_cow_list = list(map(int, [*input.readline().strip("\n")]))
    one_counts = []
    count = 1
    if infected_cow_list.count(1) == n:
        print(1)
        return
    
    sectional = 0
    for i in range(n):
        if infected_cow_list[i] == 1 and infected_cow_list[i+1] == 0:
            one_counts.append(infected_cow_list[sectional:i+2].count(1))
            sectional = i + 1
    
    if infected_cow_list.count(1) != n:
        minimum_ones = min(one_counts)
        sum = 1
    else:
        print(infected_cow_list.count(1))
        return
    
    
    if infected_cow_list[-1] == 1:
        one_counts.append(1)
    
    # print(one_counts) # remove

    for i in one_counts:
        sum += num_base_ones(i, minimum_ones)

    print(sum)

def num_base_ones(one_count, minimum_ones):
    if minimum_ones != one_count and minimum_ones != 1:
        if minimum_ones % 2 == 1:
            return one_count//minimum_ones + 1
        else:
            return one_count//(minimum_ones + 1) + 1
    elif minimum_ones != one_count and minimum_ones == 1:
        if minimum_ones % 2 == 1:
            return one_count//minimum_ones
        else:
            return one_count//(minimum_ones + 1)
    else:
        return 0
 
main()
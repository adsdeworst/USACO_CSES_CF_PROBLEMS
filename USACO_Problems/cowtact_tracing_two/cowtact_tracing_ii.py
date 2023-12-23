import sys

def main():
    input = sys.stdin
    output = sys.stdout

    n = int(input.readline())
    infected= list(map(int, [*input.readline().strip("\n")]))
    ones_list = []
    count_list = []

    sum = 0
    if infected[0] == 0:
        status = False
    else:
        status = True

    temp_list = ""
    for i in range(infected.index(1), n):
        if infected[i] == 1:
            temp_list += "1"
        elif infected[i] == 0:
            if len(temp_list) != 0:
                count_list.append(len(temp_list))
            temp_list = ""

    if len(temp_list) != 0:
        count_list.append(len(temp_list))
    temp_list = ""

    minimum_count = min(count_list)
    count_list.pop(count_list.index(minimum_count))
    days = 0

    if minimum_count%2 == 0:
        sum = 2
    else:
        sum = 1
    
    temp = minimum_count
    while temp != 1 and temp != 2:
        temp -= 2
        days += 1

    for i in range(len(count_list)):
        if count_list[i] % 2 == 1:
            sum += count_list[i]//(days + 1)
        else:
            sum += count_list[i]//(days + 1)

    print(sum)

main()
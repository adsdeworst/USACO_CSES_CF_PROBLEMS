import sys
from math import ceil

def main():
    fin = sys.stdin
    test_cases = int(fin.readline().strip("\n"))
    answers = []
    for _ in range(test_cases):
        answers.append(days_to_make_bigger(int(fin.readline().strip("\n")), list(map(int, fin.readline().strip("\n").split())), list(map(int, fin.readline().strip("\n").split())), list(map(int, fin.readline().strip("\n").split()))))
    
    for i in answers:
        print(i)

def days_to_make_bigger(n, h, a, t):
    # n  = number of plants
    # h = initial heights of each plant
    # a = number of inches the plant grows
    # t = hierarchy
    hierarchy_list = [0]*n
    for i in range(n):
        temp = [h[i], a[i], t[i]]
        hierarchy_list[n  - 1 - t[i]] = temp
    
    count = 0
    for i in range(n - 1):
        if hierarchy_list[i][0] + hierarchy_list[i][1] * count >= hierarchy_list[i+1][0] + hierarchy_list[i + 1][1] * count:
            if hierarchy_list[i][1] >= hierarchy_list[i+1][1]:
                return -1
            else: # hierarchy_list[i+1][1] > hierarchy_list[i][1]
                # h + ax = h + ax
                days = (hierarchy_list[i][0] + count * hierarchy_list[i][1]) - (hierarchy_list[i + 1][0] + hierarchy_list[i + 1][1] * count)
                days = days/(hierarchy_list[i + 1][1] - hierarchy_list[i][1])
                count += ceil(days)

                if (hierarchy_list[i][0] + count * hierarchy_list[i][1] == hierarchy_list[i+1][0] + hierarchy_list[i+1][1] * count):
                    count += 1
        else:
            continue

    return count

main()
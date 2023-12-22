import sys

def main():
    for i in range(int(sys.stdin.readline().strip("\n"))):
        print(get_days(int(sys.stdin.readline().strip("\n")), list(map(int, sys.stdin.readline().strip("\n").split())), list(map(int, sys.stdin.readline().strip("\n").split())), list(map(int, sys.stdin.readline().strip("\n").split()))))

def get_days(n, h, a, t):
    days = 0
    while not check_if_satisfied(n, h, t):
        days += 1
        h = add_lists(n, h, a)
        if days > 1000:
            return -1
    return days

def add_lists(n, list_one, list_two):
    result = []
    for i in range(n):
        result.append(list_one[i] + list_two[i])

    return result

def check_if_satisfied(n, h, t):
    sorted_h = sorted(h)
    status = True
    for i in range(n):
        while status:
            plant_height = h[i]
            if len(sorted_h[0:sorted_h.index(plant_height)]) == n - t[i]:
                continue
            else:
                status = False
                return status
    
    return status

print(get_days(2, [2, 1], [1, 3], [1, 0]))
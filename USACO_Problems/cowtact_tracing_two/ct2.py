import sys
import math

def main():
    n = int(sys.stdin.readline().strip("\n")) # int
    cows = sys.stdin.readline().strip("\n") # string
    cow_counts = [] # int

    if "1" not in cows:
        print(0)
        return

    count = 0
    for i in range(n):
        if cows[i] == "0" and count > 0:
            cow_counts.append(count)
            count = 0
        elif cows[i] == "1":
            count += 1       
    
    L = len(cow_counts)
    max_days = get_days(min(cow_counts[1:L]))
    left_zero = cow_counts[0] == 0
    right_zero = cow_counts[L - 1] == 0

    if left_zero:
        if cow_counts[0] - 1 == min(max_days, cow_counts[0] - 1):
            max_days = cow_counts[0] - 1
    
    if right_zero:
        if cow_counts[L - 1] - 1 == min(max_days, cow_counts[L - 1] - 1):
            max_days = cow_counts[L - 1] - 1       

    count = 0
    for k in range(len(cow_counts)):
        count += math.ceil(cow_counts[k]/(2* max_days + 1))

    print(count)
    return

def get_days(count):
    days = 1
    while count != 2 or count != 1:
        count -= 2
        days += 1

    return days

if __name__ == "__main__":
    main()
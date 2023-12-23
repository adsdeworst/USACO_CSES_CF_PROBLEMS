import sys
import math

def main():
    n = int(sys.stdin.readline().strip("\n")) # int
    cows = sys.stdin.readline().strip("\n") # string
    cow_counts = [] # int

    count = 0
    for i in range(n):
        if cows[i] == "0" and count > 0:
            cow_counts.append(count)
            count = 0
        elif cows[i] == "1":
            count += 1       
        
    minimum = min(cow_counts)
    minimum = get_days(minimum)

    for k in range(len(cow_counts)):
        cow_counts[k] = math.ceil(cow_counts[k]/(2* minimum + 1))

    print(sum(cow_counts))

def get_days(count):
    days = 1
    while count != 2 or count != 1:
        count -= 2
        days += 1

    return days

if __name__ == "__main__":
    main()
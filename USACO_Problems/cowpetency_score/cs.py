import sys

def main():
    continue

def cowpetency(cows, intervals, max_c, cow_list, interval_list):
    for i in interval_list:
        a, h = i
        start = max(cow_list[:a + 1])
        mid = max(cow_list[a+1:h])
        
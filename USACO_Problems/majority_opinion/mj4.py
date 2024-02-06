import sys
from collections import Counter

def get_num(length, list):
    h_length = length//2 + 1
    counts = Counter(list)
    results = []
    for key in counts.keys():
        if counts[key] >= h_length:
            results.append(key)
    
    return results

def check(length, list):
    if length == 1:
        return [list[0]]
    if length == 2:
        if list[0] == list[1]:
            return [list[0]]
        else:
            return[-1]
        
    h_length = max(3, length//2 + 1)
    results = set()
    for i in range(length - h_length + 1):
        for k in get_num(h_length, list[i:i+h_length + 1]):
            results.add(k)
    
    if len(results) == 0:
        results.add(-1)
    return results

def main():
    for i in range(int(sys.stdin.readline().strip("\n"))):
        new_list = list(check(int(sys.stdin.readline().strip("\n")), list(map(int, sys.stdin.readline().strip("\n").split()))))
        new_list = sorted(new_list)

        string = ""
        for i in new_list:
            string += str(i) + " "
        
        if string[-1] == " ":
            string = string[:-1]
        
        print(string)

main()
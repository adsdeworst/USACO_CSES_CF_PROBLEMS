import sys
from collections import Counter

def get_number(length, list):
    counts = Counter(list)
    hlength = length//2 + 1
    result = []
    for i in counts.keys():
        if counts[i] > hlength:
            result.append(i)
    
    return result

def check(length, list):
    hlength = max(3, length//2 + 1)
    result = set()
    for i in range(max(1, length - hlength)):
        for k in get_number(hlength, list[i:i+hlength]):
            result.add(k)
    
    if len(result) == 0:
        result.add(-1)
    
    return result

print(check(3, [3, 2, 3]))
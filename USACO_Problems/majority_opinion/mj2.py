import sys
from collections import Counter

def get_all_substrings(input_list):
    if len(input_list) == 0:
        return []
    elif len(input_list) == 1:
        return [input_list]
    else:
        output = []
        for i in range(len(input_list)):
            for j in range(i+1, len(input_list)+1):
                output.append(input_list[i:j])

        return output + get_all_substrings(input_list[1:])
    
def find_possible_hays(n, preferences):
    hay_count = Counter(preferences)
    potential_hays = []
    for hay in hay_count.keys():
        if hay_count[hay] > n // 2:
            potential_hays.append(hay)
    if not potential_hays:
        return [-1]
    return sorted(set(potential_hays))

outputs = []

for i in get_all_substrings([1, 1, 2, 2]):
    output = find_possible_hays(len(i), i)
    print(i)
    print(output)
    print("\n")

    if len(i) > 2:
        outputs.append(output)

print(outputs)
    
# for i in outputs:



# def main():
#     for i in range(int(sys.stdin.readline().strip("\n"))):
#         length = int(sys.stdin.readline().strip("\n"))
#         string = 
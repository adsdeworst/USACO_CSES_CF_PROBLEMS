# import sys

# def main():
#     n = int(sys.stdin.readline().strip("\n"))
#     string = sys.stdin.readline().strip("\n")
# #     count = 0
# #     for i in range(2, n):
# #         if is_lonely(string[i - 2 : i + 1]):
# #             count += 1
    
# #     print(count)
# #     return
# # main()
    
import sys
n = int(sys.stdin.readline().strip("\n"))
orig_string = sys.stdin.readline().strip("\n")
count = 0

def is_lonely(my_string): 
    if my_string.count("H") == 1 or my_string.count("G") == 1:
        return True
    return False

def it(word, count = 0):
    set1 = set()
    for begin in range(len(word)):
        for end in range(begin,len(word)):
            set1.add(word[begin:end+1])
            if len(word[begin:end+1]) >= 3 and is_lonely(word[begin:end+1]):
                count += 1
    return set1 , count


temp, count = it(orig_string)
print(count)
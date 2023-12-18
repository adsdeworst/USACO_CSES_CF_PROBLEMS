import sys

def main():
    file_in = open("sleepy.in", 'r')
    sys.stdout = open("sleepy.out", 'w')

    num_ints = int(file_in.readline().strip("\n"))
    num_list = list(map(int, file_in.readline().strip("\n").split()))

    changes = num_ints - 1
    for i in range(num_ints-2, -1, -1):
        if num_list[i] < num_list[i+1]: # if in ascending, set to i
            changes = i
        else:
            break
    
    print(changes)
    return changes

main()
import sys

def main():
    input = sys.stdin
    output = sys.stdout

    # input = open("USACO_Problems\\photoshoot\\input_file.in", "r")

    n = int(input.readline())
    cows = input.readline().strip("\n")
    converted_cow = []
    key = {"HG" : True, "GH" : False}

    # print(cows)

    # for i in range(n - 1, -1, -1):
    #     if i % 2 != 1 and cows[i] == 'G':
    #         cows[0:i+2] = reversed(cows[0:i+2])
    #         count += 1

    # output.write(str(count))

    for i in range(0, n, 2):
        if (cows[i:i+2] != "GG" and cows[i:i+2] != "HH"):
            converted_cow.append(key[cows[i:i+2]])

    if converted_cow[-1] == False:
        count = 1
    else: 
        count = 0


    for i in range(0, len(converted_cow) - 1, 1):
        if converted_cow[i] != converted_cow[i + 1]:
            count += 1
    
    print(count)
    return count

# def swap(list, index):
#     for i in range(index + 1):
#         if list[i] == True:
#             list[i] = False
#         else:
#             list[i] = True

#     return list 


main()
import sys

def main():
    sys.stdout = open("taming.out", 'w')
    file_in =  open("taming.in", 'r')

    # sys.stdout = open("USACO_Problems\\taming_the_herd\\taming.out", 'w')
    # file_in =  open("USACO_Problems\\taming_the_herd\\taming.in", 'r')


    n = int(file_in.readline().strip("\n")) - 1
    uncertain_list = list(map(int, file_in.readline().strip("\n").split()))
    uncertain_list[0] = 0

    for i in range(n - 1, -1, -1):
        if uncertain_list[i + 1] > 0:
            # if not (uncertain_list[i] > 0):
            #     print(-1)
            #     return 
            if uncertain_list[i] > 0 and uncertain_list[i] != uncertain_list[i+1] - 1:
                print("-1")
                return
            
            if uncertain_list[i] > i:
                print("-1")
                return
            
            uncertain_list[i] = uncertain_list[i + 1] - 1

    negative_ones = 0
    zeros = 0

    for i in range(n + 1):
        if uncertain_list[i] == 0:
            zeros += 1
        elif uncertain_list[i] == -1:
            negative_ones += 1

    print(str(zeros) + " " + str(zeros + negative_ones))
    return

main()
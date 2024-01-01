import sys

def main():
    comet = sys.stdin.readline().strip("\n")
    group = sys.stdin.readline().strip("\n")

    comet_num = 1
    for i in comet:
        comet_num *= (ord(i) - 64)
    
    group_num = 1
    for i in group:
        group_num *= (ord(i) - 64)

    if comet_num % 47 == group_num % 47:
        print("GO")
    else:
        print("STAY")


main()
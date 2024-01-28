import sys

def main():
    n = int(sys.stdin.readline().strip("\n"))
    string = sys.stdin.readline().strip("\n")
    e_list = list(map(int, sys.stdin.readline().strip("\n").split()))
    
    first_G = string.index("G")
    first_H = string.index("H")
    last_G = string[::-1].index("G")
    last_H = string[::-1].index("H")



main()
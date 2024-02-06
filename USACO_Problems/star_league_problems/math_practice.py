# def main():
#     [a, b] = list(map(int, input().strip("\n").split()))
#     e = a + 1
#     while str(2**e)[0] != str(b) and e < 62:
#         e += 1
    
#     if e < 62:
#         print(e)
#     else:
#         print(0)

# main()


# import sys
# import math

# def main():
#     n = int(sys.stdin.readline().strip("\n"))
#     [nu, d] = list(map(int, sys.stdin.readline().strip("\n").split()))
#     num = nu
#     den = d
#     for _ in range(n - 1):
#         [nu, d] = list(map(int, sys.stdin.readline().strip("\n").split()))
#         num, den = calculate_ratio(num, den, nu, d)
    
#     print(str(num) + " " + str(den))
    
# def calculate_ratio(currNum, currDen, n, d):
#     currNum = int(currNum * d + n * currDen)
#     currDen = int(currDen * d)
#     gcd = math.gcd(currNum, currDen)
#     currNum, currDen = int(currNum/gcd), int(currDen/gcd)
#     return currNum, currDen

# main()

import sys
import math

def main():
    curr_num =["."] * 10
    swaps = 0
    for _ in range(int(sys.stdin.readline().strip("\n"))):
        [cow, side] = list(map(int, sys.stdin.readline().strip("\n").split()))
        if curr_num[cow - 1] == ".":
            curr_num[cow - 1] = side
        elif curr_num[cow - 1] == 1 and side == 0:
            swaps += 1
            curr_num[cow - 1] = side
        elif curr_num[cow - 1] == 0 and side == 1:
            swaps += 1
            curr_num[cow - 1] = side

    print(swaps)

main()
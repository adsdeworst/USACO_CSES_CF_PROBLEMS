import sys
import math

def main():
    n = int(sys.stdin.readline().strip("\n"))

    while n != sum_of_div(sum_of_div(n)) or n == sum_of_div(n):
        n += 1
    
    print(str(sum_of_div(sum_of_div(n))) + " " + str(sum_of_div(n)))

def sum_of_div(num):
    sum = 0
    for i in range(1, num//2 + 1):
        if num%i == 0:
            sum += i

    return sum
    
main()
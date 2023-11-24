import sys
import datetime

def main():
    num_of_cows = int(sys.stdin.readline())
    each_willing_pay = list(map(int, sys.stdin.readline().strip("\n").split()))
    # num_of_cows = 100000
    # each_willing_pay = open("USACO_Problems\\cow_college\\test.in", 'r').readline()
    # each_willing_pay = list(map(int, each_willing_pay.split()))
    each_willing_pay = sorted(each_willing_pay)
    max, pay = get_max_revenue(num_of_cows, each_willing_pay)
    sys.stdout.write(max + " " + pay)

def get_max_revenue(num_of_cows, each_cow_willing_pay):
    max = 0
    pay = 0
    for i in range(num_of_cows):
        curr_max, curr_pay = get_max_and_count(each_cow_willing_pay, i)
        if curr_max > max:
            max, pay = curr_max, curr_pay
    
    return str(max), str(pay)

def get_max_and_count(my_list, index):
    # return len(my_list[index:len(my_list)])*my_list[index], my_list[index]
    return (len(my_list) - index)*my_list[index], my_list[index]

if __name__ == "__main__":
    main()
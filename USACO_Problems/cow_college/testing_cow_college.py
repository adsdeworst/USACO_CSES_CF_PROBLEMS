import sys
import datetime
import random

def main():
    num_of_cows = 100000
    print(datetime.datetime.now())
    each_willing_pay = open("USACO_Problems\\cow_college\\test.in", 'r').readline()
    #for i in range(num_of_cows):
    #    each_willing_pay.append(random.randint(0, 1000000))
    each_willing_pay = list(map(int, each_willing_pay.split()))
    each_willing_pay = sorted(each_willing_pay)

    prog_start_time = datetime.datetime.now()
    max, pay = get_max_revenue(num_of_cows, each_willing_pay)
    sys.stdout.write(max + " " + pay + "\n")
    prog_end_time = datetime.datetime.now()
    print("prog processing time: " + str(prog_end_time - prog_start_time))


    

def get_max_revenue(num_of_cows, each_cow_willing_pay):
    max = 0
    pay = 0
    for i in range(num_of_cows):
        curr_max, curr_pay = get_max_and_count(each_cow_willing_pay, i, num_of_cows)
        if curr_max > max:
            max, pay = curr_max, curr_pay
    
    return str(max), str(pay)

def get_max_and_count(my_list, index, num_of_cows):
    return (num_of_cows-index)*index, my_list[index]

if __name__ == "__main__":
    main()
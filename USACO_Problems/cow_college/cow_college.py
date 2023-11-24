import sys

def get_max_tuition(num_cows, each_cow_tuition):
    max_tuition = -1
    set_tuition = 0
    distinct_tuitions = set()
    for i in each_cow_tuition:
        distinct_tuitions.add(i)
    distinct_tuitions = sorted(distinct_tuitions)
    checking_list = []
    current_index = len(distinct_tuitions)//2
    checking_list.append(distinct_tuitions[current_index])
    for i in range(1, len(distinct_tuitions)//2):
        checking_list.append(distinct_tuitions[current_index-i])
        checking_list.append(distinct_tuitions[current_index+i])

    for j in checking_list:
        total_revenue, tuition = will_attend_or_not(j, each_cow_tuition)
        if total_revenue > max_tuition:
            max_tuition = total_revenue
            set_tuition = tuition
    
    return str(max_tuition), str(set_tuition)

def will_attend_or_not(current_tuition, each_cow_tuition):
    count = 0
    for i in each_cow_tuition:
        if i >= current_tuition:
            count += 1
    
    return count*current_tuition, current_tuition

def main():
    total_num_of_cows = int(input().strip("\n"))
    each_cow_tuition = list(map(int, input().strip("\n").split()))
    max_tuition, attnding_cows = get_max_tuition(total_num_of_cows, each_cow_tuition)
    sys.stdout.write(max_tuition + " " + attnding_cows)

if __name__ == "__main__":
    main()
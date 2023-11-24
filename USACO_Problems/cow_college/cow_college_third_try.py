import sys

def get_counts(list):
    unique_item_dict = {}
    for i in list:
        if i in unique_item_dict:
            unique_item_dict[i] += 1
        else:
            unique_item_dict[i] = 1

    return unique_item_dict 

def get_tuition(item_with_counts_dictionary):
    revenue = 0
    tuition = 1
    for i in item_with_counts_dictionary:
        current_count = 0
        current_count += item_with_counts_dictionary[i:len(item_with_counts_dictionary)]
        current_tuition = i
        if current_count * current_tuition > revenue:
            revenue = current_count * current_tuition
            tuition = current_tuition

    return revenue, tuition

def main():
    num_of_cows = int(input())
    each_willing_pay = list(map(int, input().strip("\n").split()))
    max, pay = get_tuition(get_counts(each_willing_pay))
    sys.stdout.write(str(max) + " " + str(pay))

if __name__ == "__main__":
    main()
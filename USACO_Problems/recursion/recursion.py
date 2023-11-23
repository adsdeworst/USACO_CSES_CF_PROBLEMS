my_array = [1, 2, 3, 4, 5]
def print_array(index):
    if index < len(my_array):
        print(my_array[index], end = " ")
        return print_array(index+1)

print_array(0)
print("", end = "\n")
#Sum of all odd and even integers

def sum_of_o_e_int(index_two, sum_odd = 0, sum_even = 0):
    if index_two != len(my_array):
        if my_array[index_two] % 2 == 1:
            sum_odd += my_array[index_two]
            return sum_of_o_e_int(index_two+1, sum_odd, sum_even)
        else:
            sum_even += my_array[index_two]
            return sum_of_o_e_int(index_two+1, sum_odd, sum_even)
    else:
        print(sum_even, sum_odd)

sum_of_o_e_int(0)
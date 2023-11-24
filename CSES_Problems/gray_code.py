all_bit_lists = []

def get_gray_code(current_count, current_string, total_count):
    if current_count == total_count:
        my_string = ""
        for i in current_string:
            my_string += i
        #print(my_string)
        all_bit_lists.append(my_string)
        return current_string
    else:
        current_string.append("0")
        get_gray_code(current_count+1, current_string, total_count)

        current_string.pop()
        current_string.append("1")
        get_gray_code(current_count+1, current_string, total_count)
            
        current_string.pop()

final_count = int(input())
get_gray_code(0, [], final_count)
all_bit_lists = sorted(all_bit_lists)
for i in all_bit_lists:
    print(i)
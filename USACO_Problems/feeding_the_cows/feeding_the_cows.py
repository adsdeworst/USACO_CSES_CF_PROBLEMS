# Problem: 2022 December Bronze Problem #2
# Link: http://www.usaco.org/index.php?page=viewproblem2&cpid=1252 

# def get_patches(cow_locations, num_cows, max_steps): #Cow Locations: GHHGG, Num Cows: 5, Max Steps: 3
all_G_perms = []
def get_perms(current_string, original_string, is_included, total_length): # current_string = G...., GG..., GGG.., GGGG., GGGGG
    if len(current_string) == total_length:
        my_string = ""
        for i in current_string:
            my_string+=str(i)
        all_G_perms.append(my_string)
    else:
        for i in range(total_length):
            if i > 0 and original_string[i] == original_string[i-1] and not is_included[i-1]:
                continue
            current_string.append(original_string[i])
            is_included[i] = True
            get_perms(current_string, original_string, is_included, total_length)

            current_string.pop()
            is_included[i] = False
    return all_G_perms


get_perms([], ["G", ".", ".", "."], [False]*4, 4) # Remove Later
print(all_G_perms) # Remove Later


def remove_letter_in_string(string, letter= "G" or "H"):
    my_string = ""
    for i in string:
        if i != letter:
            my_string += "."
        else:
            my_string += i
    
    return my_string


def get_indexes_of_letter(total_length, string, letter = "G" or "H"):
    index_list = []
    for i in range(total_length):
        if string[i] == letter:
            index_list.append(i)
    
    return index_list

# def possibility(original_string, given_string, max_number_of_steps, total_length, key = "G" or "H"):# given_string = G...., original_string = GHHG
#     if key == "G":
#         check_string = remove_letter_in_string(original_string, key)
#         given_string_loc = get_indexes_of_letter(total_length, given_string, "G")
#         original_string_loc = get_indexes_of_letter(total_length, check_string, "G")
#         start_one = 0
#         start_two = 0
#         status = []
#         for i in range(start_one, len(given_string_loc), 1):
#             for j in range(start_two, len(original_string_loc), 1):
#                 if abs(given_string_loc[i] - original_string_loc[j]) <= max_number_of_steps:
#                     status.append(True)
#                     start_one += 2
#                     start_two += 1
#                 else:
#                     status.append(False)
        
#         for i in status:
#             if i != True:
#                 return False
#         return True

# print(possibility("GHHG", "G...", 1, 4, "G"))
# print(possibility("GHHG", "G.G.", 1, 4, "G"))
all_perms = []

def make_perm(original_string, curr_string, in_curr_string):
    if len(original_string) == len(curr_string):
        my_string = ""
        for i in curr_string:
             my_string += i
        all_perms.append(my_string)
        return curr_string
    else:
        for i in range(len(original_string)):
                if in_curr_string[i] == False:
                    if i > 0 and original_string[i] == original_string[i - 1] and not in_curr_string[i - 1]:
                        continue
                    curr_string.append(original_string[i])
                    in_curr_string[i] = True
                    make_perm(original_string, curr_string, in_curr_string)

                    curr_string.pop()
                    in_curr_string[i] = False
actual_string = input()
is_in_curr_string = len(actual_string) * [False]
make_perm(sorted(actual_string), [], is_in_curr_string)

print(len(all_perms))
for i in all_perms:
    print(i)
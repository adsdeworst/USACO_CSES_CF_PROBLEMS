my_str = input()

my_list = []
my_letter = ""
count = 1
for i in my_str:
    if my_letter == i:
        count += 1
    else:
        my_list.append(count)
        count = 1
        my_letter = i
    my_list.append(count)
print(max(my_list))
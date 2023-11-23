input_list = [1, 2, 3, 8, 6, 4]
def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list[0:len(unsorted_list)-1])):
        if unsorted_list[i]>unsorted_list[i+1]:
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[i+1]
            unsorted_list[i+1] = temp
        #else:
        #    temp = unsorted_list[i+1]
        #    unsorted_list[i+1] = unsorted_list[i]
        #    unsorted_list[i] = temp
        status = True
    for k in range(len(unsorted_list[0:len(unsorted_list)-1])):
        if unsorted_list[k] > unsorted_list[k+1]:
            status = False
            break
        else:
            status = True 

    if status == False:
        bubble_sort(unsorted_list)
    else:
        sorted_list = unsorted_list
        return sorted_list 

my_list = bubble_sort(input_list)
print(my_list)
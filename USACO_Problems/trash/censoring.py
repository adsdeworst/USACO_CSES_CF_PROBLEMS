def main():
    with open('censoring.in', 'r') as f:
        selected_string = f.readline().strip("\n")
        checking_string = f.readline().strip("\n")
        answer_string = ""
        index = 0
        occurence_of_prev_letter = None
        first_occurance = None


    while (checking_string in selected_string) == True or index != len(selected_string):
        if selected_string[index] == checking_string[0]:
            if selected_string[index:index+len(checking_string)] == checking_string:
                answer_string += ""
                selected_string = answer_string + selected_string[index+len(checking_string):len(selected_string)]
                if occurence_of_prev_letter == None:
                    index = first_occurance
                    answer_string = selected_string[0:first_occurance+1]
                else:
                    index = occurence_of_prev_letter- 1
                    answer_string = selected_string[0:occurence_of_prev_letter]
            else:
                answer_string += selected_string[index]
                if occurence_of_prev_letter == None:
                    first_occurance = index - 1
                else:
                    occurence_of_prev_letter = index - 1
        else:
            answer_string += selected_string[index]
        index += 1

    print(answer_string)

    # while i != total_lenght and k < 50:
    #     if selected_string[i] == checking_string[0]:
    #         if selected_string[i:i+len(checking_string)] == checking_string:
    #             possiblities.append(i)
    #             specific_index = i - len(checking_string)
    #             answer_string += ""
    #             i = specific_index
    #             selected_string = answer_string + selected_string[specific_index+len(checking_string):total_lenght]
    #             print("answer_string = " + answer_string +", i =" + str(i) + ". ")
    #             k+=1
    #         else:
    #             answer_string += selected_string[i]
    #             i+=1
    #             k+=1
    #             print("answer_string = " + answer_string +", i =" + str(i) + ". ")
    #     else:
    #         answer_string += selected_string[i]
    #         i+=1
    #         k+=1
    #         print("answer_string = " + answer_string +", i =" + str(i) + ". ")

main()
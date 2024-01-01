import sys

def main():
    with sys.stdin as f:
        num_of_lines = int(f.readline().strip("\n"))
        board_list = []
        for _ in range(num_of_lines):
            board_list.append(f.readline().strip("\n").split())

    one_side_board_list = []
    another_side_board_list = []
    count_list = make_list(26)  
    for k in range(num_of_lines):
        one_side_board_list.append(board_list[k][0])
        another_side_board_list.append(board_list[k][1])

    for i in range(num_of_lines):
        single_word_one_side_count_list = count_letters(one_side_board_list[i])
        single_word_another_side_count_list = count_letters(another_side_board_list[i])

        for k in range(26):
            count_list[k] += max(single_word_one_side_count_list[k], single_word_another_side_count_list[k])
    
    with sys.stdout as f:
        for i in count_list:
            f.write(str(i) + "\n")

def make_list(length):
    list = []
    for _ in range(length):
        list.append(0)

    return list

def count_letters(word):
    count_list = []
    for i in range(26):
        count_list.append(0)

    for i in word:
        count_list[ord(i)-97] += 1

    return count_list

main()
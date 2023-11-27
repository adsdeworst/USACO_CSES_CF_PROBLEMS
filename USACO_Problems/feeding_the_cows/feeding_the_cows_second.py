import sys

def optimize(my_string, step_size):
    length = len(my_string)
    #step_size = int(step_size)
    result_string = ["."] * length
    result = ""
    found = False

    if step_size != 0 and length != 2:
        for i in range(length):
            found = False
            if (i+step_size) >= length and (i-step_size) <= 0:
                for j in range(0, length):
                    if result_string[j] == my_string[i]:
                        found = True
                        break
                if found:
                    continue
                for j in range(length-1, 0, -1):
                    if result_string[j] == ".":
                        result_string[j] = my_string[i]
                        break
                    else:
                        continue

            elif (i+step_size) >= length:
                for j in range(i-step_size, length):
                    if result_string[j] == my_string[i]:
                        found = True
                        break
                if found:
                    continue
                for j in range(length - 1, 0, -1):
                    if result_string[j] == ".":
                        result_string[j] = my_string[i]
                        break
                    else:
                        continue

            elif (i-step_size) <= 0:
                for j in range(0, i+step_size):
                    if result_string[j] == my_string[i]:
                        found = True
                        break
                if found:
                    continue
                for j in range(i+step_size, 0, -1):
                    if result_string[j] == ".":
                        result_string[j] = my_string[i]
                        break
                    else:
                        continue

            else:
                for j in range(i-step_size, i+step_size):
                    if result_string[j] == my_string[i]:
                        found = True
                        break
                if found:
                    continue
                for j in range(i+step_size, i-step_size, -1):
                    if result_string[j] == ".":
                        result_string[j] = my_string[i]
                        break
                    else:
                        continue

        count = 0               
        for i in result_string:
            if i != ".":
                count += 1
            result += i

        return count, result
    
    else:
        return length, my_string
    
def main():
    test_case = int(sys.stdin.readline())
    length_and_step_size = []
    all_my_strings = []
    for i in range(test_case):
        length_and_step_size.append(list(map(int, sys.stdin.readline().strip("\n").split())))
        all_my_strings.append(sys.stdin.readline().strip("\n"))
        # [length,  step_size] = list(map(int, sys.stdin.readline().strip("\n").split()))
        # my_string = sys.stdin.readline().strip("\n")
        # for i in optimize(my_string, length, step_size):
        #     sys.stdout.write(str(i) + "\n")
    
    for l in range(test_case):
        [length, step_size] = length_and_step_size[l]
        my_string = all_my_strings[l]
        for w in optimize(my_string, int(length), step_size):
            sys.stdout.write(str(w) + "\n")

main()
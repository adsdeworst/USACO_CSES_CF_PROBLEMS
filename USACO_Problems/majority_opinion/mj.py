import sys

def main():
    result = []
    temp_string = ""
    for i in range(int(sys.stdin.readline())):
        for k in check(sys.stdin.readline(), sys.stdin.readline()):
            temp_string += str(k) + " "
        result.append(temp_string)
        temp_string = ""

    for i in result:
        print(i)

def check(length, string) -> list:
    result = []
    length = int(str(length).strip("\n"))
    string = sorted(list(map(int, str(string).strip("\n").split())))

    if length == 2:
        return [-1]

    if length % 2 == 1: 
        length = length//2 + 1
    else:
        length = length//2
    current_num = string[0]
    count = 1
    for i in range(1, len(string)):
        if current_num != string[i]:
            if count >= length:
                result.append(current_num)
            current_num = string[i]
            count = 1
        else:
            count += 1

    if count >= length:
        result.append(current_num)
    current_num = string[i]
    count = 1
    
    if len(result) == 0:
        return [-1]
    else:
        return result
    

main()
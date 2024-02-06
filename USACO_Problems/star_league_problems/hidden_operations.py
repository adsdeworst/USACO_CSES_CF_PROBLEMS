import sys

def main():
    my_string = sys.stdin.readline().strip("\n")

    operation_str = ""
    for i in my_string:
        if not i.isalpha():
            operation_str += i
        
        if i.isalpha() and len(operation_str) > 0:
            print(int(operation(str(operation_str))), end=" ")
            operation_str = ""


def operation(string = str):
    if "+" in string:
        [term_1, term_2] = string.split("+")
        return int(term_1) + int(term_2)
    
    elif "-" in string:
        [term_1, term_2] = string.split("-")
        return int(term_1) - int(term_2)
    
    elif "*" in string:
        [term_1, term_2] = string.split("*")
        return int(term_1) * int(term_2)
    
    elif "/" in string:
        [term_1, term_2] = string.split("/")
        return int(term_1) / int(term_2)

main()
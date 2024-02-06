import sys

def main():
    number = sys.stdin.readline().strip("\n")

    count = 3 - len(number)%3
    string = ""

    for i in number:
        if count == 3:
            count = 1
            string += ","
            string += i
        else:
            count += 1
            string += i
    

    if string[0] == ",":
        string = string.lstrip(",")

    print(string)

main()
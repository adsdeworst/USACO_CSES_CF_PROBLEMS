import sys

def main():
    result = []
    temp_string = ""
    for i in range(int(sys.stdin.readline())):
        result.append(check(sys.stdin.readline(), sys.stdin.readline()))

    for i in result:
        print(i)

def check(length, string):
    result = []
    length = int(str(length).strip("\n"))
    string = sorted(list(map(int, str(string).strip("\n").split())))
    counts = [0]*length

    if length%2 == 1:
        dlength = length//2 + 1
    else:
        dlength = length//2

    for i in range(length):
        counts[string[i] - 1] += 1
        
    for k in range(length):
        if counts[k] >= dlength:
            result.append(k + 1)
    
    return result


main()
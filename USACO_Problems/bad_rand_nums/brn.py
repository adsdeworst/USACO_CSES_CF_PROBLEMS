import sys

def main():
    n = int(sys.stdin.readline().strip("\n"))
    n_orig = []
    count = 0
    while len(str(n)) > 1:
        n_orig.append(n)
        if len(str(n)) == 3:
            n = str(n)[0] + str(n)[1]
            n = int(n)
            n = n**2
            count += 1
            if n in n_orig:
                print(count)
                return
        elif len(str(n)) == 4:
            n = str(n)[1] + str(n)[2]
            n = int(n)
            n = n**2
            count += 1
            if n in n_orig:
                print(count)
                return
        elif len(str(n)) == 2:
            n = str(n)[0]
            n = int(n)
            n = n**2
            count += 1
            if n in n_orig:
                print(count)
                return
    count += 2
    
    print(count)
    return


main()
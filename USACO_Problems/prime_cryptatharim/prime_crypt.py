import sys

def main():
    n = int(sys.stdin.readline().strip("\n"))
    valid_nums = list(map(int, sys.stdin.readline().strip("\n").split()))

    count = 0
    for i in valid_nums:
        orig = i
        for k in valid_nums:
            for g in valid_nums:
                for j in valid_nums:
                    for l in valid_nums:
                        i = orig
                        num_1 = 100*i + 10*k + g
                        num_2 = 10 * j + l
                        status = True
                        if len(str(num_1 * l)) <= 3 and len(str(num_1 * j)) <= 3:
                            for i in str(num_1 * l):
                                if int(i) in valid_nums and status:
                                    continue
                                else:
                                    status = False
                                    break
                            
                            for i in str(num_1 * j):
                                if int(i) in valid_nums and status:
                                    continue
                                else:
                                    status = False
                                    break
                            
                        if len(str(num_1 * num_2)) <= 4 and status:
                            for i in str(num_1 * num_2):
                                if int(i) in valid_nums:
                                    continue
                                else:
                                    status = False
                                    break

                        if status == True:
                            count += 1
                    else:
                        break

    print(count)

main()
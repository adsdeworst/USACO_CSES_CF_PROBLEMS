def counting_cows_in_region(cows, a, b):
    cows_in_region = [0,0,0,0]
    for cow in cows:
        if cow[0] < a and cow[1] < b:
            cows_in_region[0] += 1
        elif cow[0] > a and cow[1] < b:
            cows_in_region[1] += 1
        elif cow[0] > a and cow[1] > b:
            cows_in_region[2] += 1
        else:
            cows_in_region[3] += 1

    return cows_in_region

def main():
    with open("balancing.in", "r") as f:
        n, b = map(int, f.readline().split())
        cows = []
        for _ in range(n):
            cows.append(list(map(int, f.readline().split())))
   
    possible_a_values = []
    possible_b_values = []
    for cow in cows:
        if ((cow[0] - 1) in possible_a_values) is False:
            possible_a_values.append(cow[0] - 1)
        elif ((cow[0] + 1) in possible_a_values) is False:
            possible_a_values.append(cow[0] + 1)

        if ((cow[1] - 1) in possible_b_values) is False:
            possible_b_values.append(cow[1] - 1)
        elif ((cow[1] + 1) in possible_b_values) is False:
            possible_b_values.append(cow[1] + 1)

    M = n
    for a in possible_a_values:
        for b in possible_b_values:
            M = min(M, max(counting_cows_in_region(cows, a, b)))
    
    with open("balancing.out", "w") as f:
        f.write(str(M))
    
if __name__ == "__main__":
    main()
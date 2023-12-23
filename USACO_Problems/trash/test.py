def find_initial_infected(cow_line):
    n = len(cow_line)
    initial_infected = 0
    
    for i in range(n):
        # Check if the current cow is infected
        if cow_line[i] == '1':
            # Check if the left and right neighbors (if they exist) are uninfected
            if (i == 0 or cow_line[i-1] == '0') and (i == n-1 or cow_line[i+1] == '0'):
                initial_infected += 1
                # Mark the right neighbor as infected to avoid double counting
                if i < n-1:
                    cow_line[i+1] = '1'

    return initial_infected

cow_line = list("011101")  # Convert string to a list for easy modification
print(find_initial_infected(cow_line))
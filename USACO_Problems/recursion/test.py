def print_subsets(arr, k, subset):
    if k == len(arr):
        print(subset)
    else:
        # Exclude the current element
        print_subsets(arr, k + 1, subset)
        
        # Include the current element
        subset.append(arr[k])
        print_subsets(arr, k + 1, subset)
        subset.pop()  # Remove the last element to backtrack

# Example usage:
arr = [1, 2, 3]
subset = []
print_subsets(arr, 0, subset)


def search(k):
    if k == n:
        # Process subset
        print(k)
        pass  # Replace this with your subset processing code
    else:
        search(k + 1)
        subset.append(k)
        search(k + 1)
        subset.pop()

# Define 'n' and 'subset' before calling the search function
n = 5  # Replace with your desired value for 'n'
subset = []  # Initialize an empty list for the subset

# Call the search function with the initial value of 'k'
search(0)

def generate_subsets(arr):
    if len(arr) == 0:
        return [[]]

    subsets = generate_subsets(arr[:-1])
    last_element = arr[-1]

    new_subsets = []
    for subset in subsets:
        new_subsets.append(subset + [last_element])

    return subsets + new_subsets

input_list = [0, 1, 2]
all_subsets = generate_subsets(input_list)

print(all_subsets)

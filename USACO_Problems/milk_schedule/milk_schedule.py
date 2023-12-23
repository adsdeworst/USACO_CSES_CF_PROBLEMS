import sys

def main():
    [n, q] = list(map(int, sys.stdin.readline().strip("\n").split()))
    cows = [0]
    questions = []

    for _ in range(n):
        cows.append(int(sys.stdin.readline().strip("\n")))

    for _ in range(q):
        questions.append(int(sys.stdin.readline().strip("\n")))

    for i in range(1, n+1):
        cows[i] = cows[i-1] + cows[i]
    
    for j in questions:
        print(binary_search(cows, 0, n, j))


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.
 
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if (arr[mid] > x >= arr[mid - 1]):
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

main()
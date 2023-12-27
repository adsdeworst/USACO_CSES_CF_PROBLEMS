import sys

def main():
    [n, k] = list(map(int, sys.stdin.readline().strip("\n").split()))
    location = [0] * 1000000

    for _ in range(n):
        [g, x] = list(map(int, sys.stdin.readline().strip("\n").split()))
        location[x] = g

    curr_sum = sum(location[0:k])
    max_sum = curr_sum

    for i in range(0, 1000000):
        L = i - k
        R = i + k
        if L < 0:
            curr_sum += location[R]
        elif R >= 999999:
            curr_sum -= location[L]
        else:
            curr_sum += location[R]
            curr_sum -= location[L - 1]

        if curr_sum > max_sum:
            max_sum = curr_sum

    print(max_sum)

main()



# import sys

# def main():
#     [n, k] = list(map(int, sys.stdin.readline().strip("\n").split()))
    
#     single_loc = []

#     max_x = 0
#     for _ in range(n):
#         [g, x] = list(map(int, sys.stdin.readline().strip("\n").split()))
#         if x > max_x:
#             max_x = x
#         single_loc.append([g, x])

#     loc = [0]*(max_x)
#     for i in single_loc:
#         [g, x] = i
#         loc[x - 1] = g


#     curr_sum = sum(loc[0:k])
#     max_sum = curr_sum

#     for i in range(1, max_x):
#         L = max(i - k - 1, 0)
#         R = min(i + k + 1, max_x - 1)
#         curr_sum = sum(loc[L:R])
#         if curr_sum > max_sum:
#             max_sum = curr_sum    
#     print(max_sum)

# main()
import sys
from collections import deque

sys.stdin = open("USACO_Problems/bovine_acrobatics/input.in", "r")

n, m, k = list(map(int, input().strip("\n").split()))
cow_weight = []
for _ in range(n):
    cow_weight.append(list(map(int, input().strip("\n").split())))
    
cow_weight.sort(key=lambda x:x[0], reverse=True)
cow_weight = deque(cow_weight)

# n = number of different weights
# m = number of towers
# k = difference to be considered 

result = deque([])
result.append([10e8, m])
count = 0
i = 0
# while count < m:
#     weight, number = cow_weight[i]
#     if count < m:
#         result.append([weight, min(m - count, number)])
#         cow_weight[i][1] -= min(m - count, number)
#         count += min(m - count, number)
#     i += 1

final_count = 0
checker = 0
for i in range(n):
    number = cow_weight[i][1]
    count = 0
    checker = 0
    length = len(result)
    while result[checker][0] >= k + cow_weight[i][0] and number > 0:
        if number >= result[checker][1]:
            number -= result[checker][1]
            count += result[checker][1]
            
        else:
            result[checker][1] = result[checker][1] - number
            count += number
            number -= number
        checker += 1
    result.append([cow_weight[i][0] , count])
    final_count += count
    

'''
for i in range(n):
    weight, number = cow_weight[i] # unassigned cows data
    # for j in range(len(result)):
    result_length = len(result)
    j = 0
    result_length = len(result)

    while j < result_length:
        tower_weight, tower_num = result[j] # tower data
        if cow_weight[i][1] > 0 and result[j][0] >= k + cow_weight[i][0]:
            if cow_weight[i][1] >= result[j][1]:
                result[j][0] = cow_weight[i][0]
                cow_weight[i][1] -= result[j][1]
                count += result[j][1]
            else: # number < tower_num
                # stays_same = number - tower_num
                # different_to_replace = tower_num
                result[j][1] = result[j][1] - cow_weight[i][1]
                result.insert(j, [cow_weight[i][0], cow_weight[i][1]])
                result_length += 1
                j += 1
                count += cow_weight[i][1]
                break
        j += 1
'''
        
print(final_count)

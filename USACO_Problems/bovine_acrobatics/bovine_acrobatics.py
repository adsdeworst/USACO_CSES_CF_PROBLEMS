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

result = deque()
count = 0
i = 0
while count < m:
    weight, number = cow_weight[i]
    if count < m:
        result.append([weight, min(m - count, number)])
        cow_weight[i][1] -= min(m - count, number)
        count += min(m - count, number)
    i += 1
        
for i in range(n):
    weight, number = cow_weight[i] # unassigned cows data
    # for j in range(len(result)):
    result_length = len(result)
    j = 0
    while j < result_length:
        tower_weight, tower_num = result[j] # tower data
        if number > 0 and tower_weight >= k + weight:
            if number >= tower_num:
                result[j][0] = weight
                cow_weight[j][1] -= tower_num
                count += tower_num
            else: # number < tower_num
                # stays_same = number - tower_num
                # different_to_replace = tower_num
                result[j][1] = tower_num - number
                result.insert(j, [weight, number])
                result_length += 1
                count += number
        else:
            cow_weight[i][1] = 0
            break
        j += 1
    cow_weight[i][1] = 0
        
print(count)
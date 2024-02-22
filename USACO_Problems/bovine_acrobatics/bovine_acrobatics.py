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
result.append([10e9, m])
count = 0   
ind = 0
        
for i in range(ind, n):
    j = 0
    result_length = len(result)

    while j < result_length:
        if result[j][0] >= k + cow_weight[i][0]:
            """if there are more cows waiting that there are available for that specific group of towers.
            if thats the case, then amount you need to is just that specific group of towers 
            (subtract that many from the waiting)
            
            if thats not the case, then split up the selected group into two, one group being the waiting number,
            and the other being the num_orig-waiting number
            then just change the waiting number cow group type to the waiting type
            """
            
            
            
            if cow_weight[i][1] >= result[j][1]:
                result[j] = [cow_weight[i][0], result[j][1]]
                cow_weight[i][1] -= result[j][1]
                count += result[j][1]
            else: 
                result[j][1] = result[j][1] - cow_weight[i][1]
                result.insert(j, [cow_weight[i][0], cow_weight[i][1]])
                sorted(result)
                count += cow_weight[i][1]
                j += 1
        j += 1
    # print(count)
print(count)


# cow_weight[i][1] < result[j][1]
                # stays_same = cow_weight[i][1] - result[j][1]
                # different_to_replace = result[j][1]

# while count < m:
#     weight, number = cow_weight[ind]
#     if count < m:
#         if count + number > m:
#             add = m - count
#         else:
#             add = number
#         result.append([weight, add])
#         cow_weight[ind][1] -= add
#         count += add
#     ind += 1
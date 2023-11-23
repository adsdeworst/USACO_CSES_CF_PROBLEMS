n = int(input())
weight_list = list(map(int, input().strip("\n").split()))

#n = 5
#weight_list = [3, 2, 7, 4, 1]

def min_sum(i, sum1, sum2):
    if n == i:
        return abs(sum1 - sum2)
    else:
        return min(min_sum(i+1, sum1 + weight_list[i], sum2), min_sum(i+1, sum1, sum2 + weight_list[i]))
    
print(min_sum(0, 0, 0))
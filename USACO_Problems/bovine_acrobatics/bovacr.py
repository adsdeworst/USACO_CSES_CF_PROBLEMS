import sys
from collections import deque

def main():
    N, M, K = list(map(int, input().strip("\n").split()))
    counts = []
    for _ in range(N):
        counts.append(list(map(int, input().strip("\n").split())))
    resulting_counts = []
    counts = sorted(counts,key=lambda x: x[0])
    
    cow_weights = []
    num_of_cows = []
    for i in range(N):
        cow_weights.append(counts[i][0])
        num_of_cows.append(counts[i][1])
    cow_weights = deque(cow_weights)
    num_of_cows = deque(num_of_cows)
    
    result = deque([])
    col_top_nums = []
    init = 0
    while init <= M:
        first_cow_weight = cow_weights[0]
        first_cow_num = num_of_cows[0] 
        
    # status = True
    # temp = 0
    # while status:
    #     a, b = counts[-1]
    #     if b + temp > M:
    #         resulting_counts.append([a, b + temp - ((b + temp) - M)])
    #         counts[-1][1] = b - (M - temp)
    #         temp += M - temp
    #         status = False
    #     elif b + temp == M:
    #         resulting_counts.append([a, b])
    #         temp += b
    #         status = False
    #         counts.pop(-1)
    #     elif b + temp < M:
    #         resulting_counts.append([a, b])
    #         temp += b
    #         counts.pop(-1)
            
    # print(resulting_counts)
    # print(counts)
    
    # num_in_column = M
    # counts = list(reversed(counts))
    # for i in range(len(counts)):
    #     a, b = counts[0] 
    #     for k in range(len(resulting_counts)):
    #         A, B = resulting_counts[k]
    #         if A - a >= K:
    #             if B == b:
    #                 resulting_counts[k] = [a, b]
    #                 num_in_column += b
    #             elif B > b:
    #                 resulting_counts.append([A, B - b])
    #                 num_in_column += B - b
    #                 resulting_counts[k] = [a, b]
    #                 resulting_counts = list(reversed(sorted(resulting_counts, key=lambda x:x[0])))
    #                 break
    #             elif B < b:
    #                 num_in_column += B
    #                 resulting_counts[k] = [a, B]
    #                 counts[0] = [a, b - B]
    #         else:
    #             break
    #    counts.pop(0)
    
    
    
    # print(resulting_counts)
    print(num_in_column)
    
main()
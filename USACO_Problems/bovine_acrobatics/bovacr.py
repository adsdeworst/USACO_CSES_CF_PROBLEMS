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
    
    # result = deque()
    # count = 0
    # while count < M:
    #     first_cow_weight = cow_weights[0]
    #     first_cow_num = num_of_cows[0] 
    #     if first_cow_num + count >= M:
    #         result.append([first_cow_weight, M - count])
    #         num_of_cows[0] = [first_cow_weight, first_cow_num - (M - count)]
    #         count = M
    #     else: # first_cow_num <= M:
    #         result.append([first_cow_num, first_cow_weight])
    #         count += first_cow_weight
            
    #         cow_weights.popleft()
    #         num_of_cows.popleft()
    #         # since the cows are in the tower positions, remove it from line
            
    # # testing whether the initial deques give the correct inputs
    # print(cow_weights)
    # print(num_of_cows)
    
    # # now, read each top cow in tower and decide where to put it.
    # # if the difference is atleast K (which means it includes K), then you can replace the cow, and add that to count
    # # if not, then you can just assume that it wont work for the next cows so you can just break the loop there
    
    # length_after = len(cow_weights)
    # for top_cow in range(len(result)):
    #     top_cow_weight = result[top_cow][0]
    #     number_of_top_cows = result[top_cow][1]
    #     maximum_weight_req = top_cow_weight + K
    #     for _ in range(length_after):
    #         if cow_weights[0] <= maximum_weight_req:
    #             if num_of_cows[0] >= number_of_top_cows:
    #                 result[top_cow][0] = cow_weights[0]
    #                 counts += M
    #                 cow_weights.popleft()
    #                 num_of_cows.popleft()
    #             else:
    #                 # if only a couple towers can be filled with this specific new cow
    #                 # split lead and replace that lead with that head
                    
    #         else:
    #             cow_weights.popleft()
    #             num_of_cows.popleft()
    #             length_after -= 1
    #     # check if you can add to this list. 
        
        
        
        
    status = True
    temp = 0
    while status:
        a, b = counts[-1]
        if b + temp > M:
            resulting_counts.append([a, b + temp - ((b + temp) - M)])
            counts[-1][1] = b - (M - temp)
            temp += M - temp
            status = False
        elif b + temp == M:
            resulting_counts.append([a, b])
            temp += b
            status = False
            counts.pop(-1)
        elif b + temp < M:
            resulting_counts.append([a, b])
            temp += b
            counts.pop(-1)
            
    print(resulting_counts)
    print(counts)
    
    num_in_column = M
    counts = list(reversed(counts))
    for i in range(len(counts)):
        a, b = counts[0] 
        for k in range(len(resulting_counts)):
            A, B = resulting_counts[k]
            if A - a >= K:
                if B == b:
                    resulting_counts[k] = [a, b]
                    num_in_column += b
                elif B > b:
                    resulting_counts.append([A, B - b])
                    num_in_column += B - b
                    resulting_counts[k] = [a, b]
                    resulting_counts = list(reversed(sorted(resulting_counts, key=lambda x:x[0])))
                    break
                elif B < b:
                    num_in_column += B
                    resulting_counts[k] = [a, B]
                    counts[0] = [a, b - B]
            else:
                break
        counts.pop(0)
    
    
    
    print(resulting_counts)
    print(num_in_column)
    
main()
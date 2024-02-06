import sys

def main():
    sys.stdin = open("div7.in","r")
    sys.stdout = open("div7.out","w")

    nums = []
    n = int(input().strip("\n"))
    for i in range(n):
        nums.append(int(input().strip("\n")))
    
    cum_freq = [0]
    tot_sum = 0
    for k in range(n):
        tot_sum += nums[k]
        cum_freq.append(tot_sum)
    
    max_num = []
    start = -1
    end = -1
    for i in range(n):
        if nums[i]%7 == 0 and start == -1:
            start = i
            continue
        
        if (nums[i] - nums[start])%7 != 0 and start != -1 and end == -1:
            end = i - 1

        if start != -1 and end != -1:
            max_num.append(end - start + 1)
            end = -1
            start = -1

    # for k in range(start + 1,n):
    #     if (cum_freq[k] - cum_freq[i])%7 == 0:
    #         if k - i > max_num:
    #             max_num = k - i
    
    print(max(max_num))

main()
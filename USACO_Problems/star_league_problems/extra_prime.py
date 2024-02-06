import sys

def main():
    [L, R] = list(map(int, sys.stdin.readline().strip("\n").split()))
    nums = []
    for i in range(L, R + 1):
        if is_prime(i):
            if is_extra_prime(i):
                nums.append(i)
    
    print(len(nums))
    print(nums[0])
    print(nums[-1])

def is_prime(num):
    i = 2
    if num == 1:
        return False
    while i*i <= num and num != 1:
        if num%i == 0:
            return False
        i += 1
    return True
    
def is_extra_prime(num):
    # for i in range(len(str(num))):
    #     num = str(num)[:i] + str(num)[i + 1:]
    #     if not is_prime(int(num)):
    #         return False
    # return True
    orig_num = num
    if len(str(orig_num)) > 2:
        for i in range(len(str(orig_num))):
            num = str(orig_num)[:i] + str(orig_num)[i + 1:]
            if not is_prime(int(num)):
                return False
        return True
    else:
        for i in range(len(str(orig_num))):
            num = str(orig_num)[i]
            if not is_prime(int(num)):
                return False
        return True

main()
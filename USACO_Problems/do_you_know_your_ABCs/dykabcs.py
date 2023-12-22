import sys

def main():
    nums = sorted(list(map(int, sys.stdin.readline().strip("\n").split())))
    a = nums[0]
    nums.pop(0)

    for i in range(6):
        if nums[i] - a in nums[:i] and nums[i] != a:
            b = nums[i] - a
            break
        elif nums[i] == a:
            b = nums[i]
            break
    
    c = nums[-1] - a - b

    print(a, b, c)

main()
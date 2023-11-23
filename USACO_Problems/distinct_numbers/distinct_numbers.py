a = set()
num_of_nums = int(input())
nums = list(map(int, input().split()))

for i in range(num_of_nums):
    a.add(nums[i])

print(len(a))
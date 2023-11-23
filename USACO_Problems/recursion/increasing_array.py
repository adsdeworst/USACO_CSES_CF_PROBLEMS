n = int(input())
my_list = list(map(int, input().split()))

counts = 0

for i in range(1, len(my_list)):
    if my_list[i] < my_list[i-1]:
        counts += (my_list[i-1]- my_list[i])
        my_list[i] = my_list[i-1]

print(counts)
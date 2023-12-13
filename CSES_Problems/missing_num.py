n = int(input())
num_list = list(map(int, input().split()))

def get_missing_num(n, num_list):
    sum = (n * (n+1)) / 2
    for i in num_list:
        sum -= i
    print(int(sum))

get_missing_num(n, num_list)
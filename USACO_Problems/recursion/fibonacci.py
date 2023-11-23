my_list = []

def fib(num):
    if num == 1 or num == 0:
        return num
    return fib(num - 1) + fib(num - 2)

for i in range(30):
    my_list.append(fib(i))

print(my_list)
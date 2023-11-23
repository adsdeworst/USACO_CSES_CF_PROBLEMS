factorial = int(input())
i = 1
zeros = 0
while 5**i < 10**9:
    zeros += factorial//5**i
    i+=1

print(zeros)
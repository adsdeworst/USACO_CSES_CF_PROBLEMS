n = int(input())
asks = []
for _ in range(n):
    asks.append(list(map(int, input().strip("\n").split())))

for i in range(n):
    y = asks[i][0]
    x = asks[i][1]
    if y>=x:
        if y%2 == 1:
            print((y-1)**2+x)
        else:
            print(y**2+1-x)
    else:
        if x%2==0:
            print((x-1)**2+y)
        else:
            print(x**2+1-y)


set_end = int(input())
sum = int(set_end*(set_end+1)/2)

if sum % 2 == 1:
    print("NO")
else:
    sum=int(sum/2)
    a = []
    b = []
    for i in range(set_end, 0, -1):
        if i <= sum:
            sum -= i
            a.append(i)
        else:
            b.append(i)

    print("YES")
    print(len(a))
    for k in a:
        print(k, end=" ")
    print("")
    print(len(b))
    for k in b:
        print(k, end=" ")
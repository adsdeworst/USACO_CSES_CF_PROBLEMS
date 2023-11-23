def main():
    with open('square.in', 'r') as f:
        [x1, y1, x2, y2] = list(map(int, f.readline().strip("\n").split()))
        [X1, Y1, X2, Y2] = list(map(int, f.readline().strip("\n").split()))

    with open('square.out', 'w') as f:
        ans = (max([max([x1, x2, X1, X2])-min([x1, x2, X1, X2]), max([y1, y2, Y1, Y2])-min([y1, y2, Y1, Y2])]))
        f.write(str(ans**2))
        print(ans)

main()
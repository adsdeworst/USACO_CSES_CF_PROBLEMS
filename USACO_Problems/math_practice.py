def main():
    [a, b] = list(map(int, input().strip("\n").split()))
    e = a + 1
    while str(2**e)[0] != str(b) and e < 62:
        e += 1
    
    if e < 62:
        print(e)
    else:
        print(0)

main()
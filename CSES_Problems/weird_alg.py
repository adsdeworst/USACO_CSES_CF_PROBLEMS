input= int(input())
def werid_alg(num):
    if num == 1:
        print(str(int(num)))
        return 1
    else:
        if num%2 == 1: #if odd
            print(str(int(num)))
            return werid_alg(num*3+1)
        else: #if even
            print(str(int(num)))
            return werid_alg(num/2)

werid_alg(input)
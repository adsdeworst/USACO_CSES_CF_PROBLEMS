def main():
    milking_amount = {"Bessie": 0, "Elsie": 0, "Daisy": 0, "Gertie": 0, "Annabelle": 0, "Maggie": 0, "Henrietta": 0}
    file_open = open("notlast.in", 'r')
    for i in range(int(file_open.readline().strip("\n"))):
        cow_milk = file_open.readline().strip("\n").split()
        milking_amount[cow_milk[0]] += int(cow_milk[1])

    minimum_amount = min(milking_amount.values())
    for i in milking_amount.keys():
        if milking_amount[i] == minimum_amount:
            milking_amount[i] = 10 ** 10

    minimum_amount = min(milking_amount.values())
    cow = ""
    count = 0
    for i in milking_amount.keys():
        if milking_amount[i] == minimum_amount:
            count += 1
            cow = i

    if count > 1:
        open("notlast.out", 'w').write("Tie")
        print("Tie")
        return "Tie"

    open("notlast.out", 'w').write(cow)
    print(cow)
    return cow


main()
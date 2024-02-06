import sys

def main():
    bronze = list(map(int, sys.stdin.readline().strip("\n").split()))
    silver = list(map(int, sys.stdin.readline().strip("\n").split()))
    gold = list(map(int, sys.stdin.readline().strip("\n").split()))
    platinum = list(map(int, sys.stdin.readline().strip("\n").split()))

    plat_prom = platinum[1] - platinum[0] # this must be the number of people decreased from gold_orig.
    gold_prom = gold[1] - (gold[0] - plat_prom)
    silver_prom = silver[1] - (silver[0] - gold_prom)

    print(silver_prom)
    print(gold_prom)
    print(plat_prom)

main()
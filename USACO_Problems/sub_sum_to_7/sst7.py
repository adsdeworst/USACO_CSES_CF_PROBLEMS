import sys

def main():
    sys.stdin = open("div7.in", 'r')
    sys.stdout = open("div7.out", 'w')
    
    cows = []
    for _ in range(int(input())):
        cows.append(int(input()))
    pref_sum = [0]
    for i in cows:
        pref_sum.append(pref_sum[-1] + i)
    
    for k in range(len(pref_sum)):
        pref_sum[k] = pref_sum[k]%7

    # print(pref_sum)

    # print(- pref_sum.index(3) + (len(pref_sum) - pref_sum[::-1].index(3) - 1))
    
    indexes = []

    for i in set(pref_sum):
        indexes.append((len(pref_sum) - pref_sum[::-1].index(i)) - pref_sum.index(i) - 1)
    
    print(max(indexes))

main()
import sys

def main():
    sys.stdin = open("maxcross.in", "r")
    sys.stdout = open("maxcross.out", "w")

    [n, k, b] = list(map(int, input().strip("\n").split()))
    broken_sigs= []
    for i in range(b):
        broken_sigs.append(int(input()))

    broken_sigs = sorted(broken_sigs)
    pref_sig_broken = [0]
    for i in range(1, n+1):
        if i in broken_sigs:
            pref_sig_broken.append(pref_sig_broken[i-1] + 1)
        else:
            pref_sig_broken.append(pref_sig_broken[i - 1])

    repairs = set()
    for i in range(k, n + 1):
        repairs.add(pref_sig_broken[i] - pref_sig_broken[i - k])

    print(min(repairs))

main()
import sys


def main():
    sys.stdin = open("bcount.in", "r")
    sys.stdout = open("bcount.out", "w")
    [N, Q] =list(map(int, input().strip("\n").split()))
    cows_list = []
    for i in range(N):
        cows_list.append(int(input()))
    temp = [0, 0, 0]
    prefix_arr = [[0,0,0]]
    for i in range(N):
        temp[cows_list[i] - 1] += 1
        prefix_arr.append(temp.copy())

    all_res = []
    for k in range(Q):
        [a,b] = list(map(int, input().strip("\n").split()))
        result = []
        for i in range(3):
            result.append(prefix_arr[b][i] - prefix_arr[a - 1][i])
        all_res.append(result.copy())

    for all in all_res:
        print(" ".join(list(map(str, all))))
        
main()
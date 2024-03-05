import sys

def main():
    sys.stdin = open("homework.in", 'r')
    sys.stdout = open("homework.out", 'w')

    n = int(input())
    scores = list(map(int, input().split()))
    scores.insert(0, 0)

    suff_sum = [0] * (1 + n + 1)
    suff_min = [10000] * (1 + n + 1)
    for i in range(n, 0, -1):
        suff_sum[i] = suff_sum[i + 1] + scores[i]
        suff_min[i] = min(suff_min[i + 1], scores[i])
        # suff_max[i] = max(suff_max[i + 1], scores[i])
        # suff_prod[i] = suff_prod[i + 1] * scores[i]

    best_score = [0, 1]
    for k in range(n - 1, 1, -1):
        #avg = (suff_sum[k] - suff_min[k]) / (n - k)
        avg = [suff_sum[k] - suff_min[k], n - k]
        # if best_score < avg:
        # if best_score[0] / best_score[1] < avg[0] / avg[1]:
        if best_score[0] * avg[1] < avg[0] * best_score[1]:
            best_score = avg
            answer = []
        # elif best_score == avg:
        if best_score[0] * avg[1] == avg[0] * best_score[1]:
            answer.append(k - 1)
    answer.reverse()
    print("\n".join(list(map(str, answer))))

main()

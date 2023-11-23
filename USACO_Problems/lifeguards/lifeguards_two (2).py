def get_difference_between(both_pairs):
    both_pairs.sort(key=lambda x: (x[0]))
    lower_pair = both_pairs[0]
    upper_pair = both_pairs[1]
    if upper_pair[0] > lower_pair[1]:
        return max(upper_pair) - min(lower_pair) - 1
    else:
        return max(upper_pair) - min(upper_pair) - 1
    
def main():
    with open('lifeguards.in', 'r') as f:
        N = int(f.readline())
        time_intervals = []
        for _ in range(N):
            time_intervals.append(list(map(int, f.readline().strip("\n").split())))
        time_intervals.sort(key=lambda x: (x[0]))
        answer_list = []

    for i in range(N):
        for k in range(i+1, N):
            both_pairs = [time_intervals[i], time_intervals[k]]
            answer_list.append(get_difference_between(both_pairs))
    with open("lifeguards.out", "w") as f:
        f.write(str(max(answer_list)))

if __name__ == "__main__":
    main()
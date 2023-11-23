def get_difference(pair_a, pair_b):
    if pair_a[1] > pair_b[0]:
        return int(max(pair_b)) - int(min(pair_a))
    elif pair_b[0] > pair_a[0] and pair_b[1] < pair_a[1]:
        return max(pair_a) - min(pair_a)
    elif pair_a[0] < pair_b[0] and pair_a[1] < pair_b[1]:
        return int(max(pair_b)) - int(min(pair_b))
    else:
        return (max(pair_a) - min(pair_a)) + (max(pair_b) - min(pair_b))
    
def main():
    with open("lifegaurds.in", "r") as f:
        N = int(f.readline())
        time_intervals = []
        for _ in range(N):
            time_intervals.append(f.readline().split())
            time_intervals.sort(key= lambda x:x[0])
        ans = 0



        for j in range(N):
            for k in range(j+1, N):
                if get_difference(time_intervals[j], time_intervals[k]):
                    if ans < abs(int(time_intervals[j][1]) - int(time_intervals[k][0])):
                        ans = abs(int(time_intervals[j][1]) - int(time_intervals[k][0]))
                else:
                    if ans < abs(time_intervals[j] - time_intervals[k]):
                        ans = abs(time_intervals[j] - time_intervals[k])

    with open("lifegaurds.out", "w") as f:
        f.write(str(ans))

if __name__ == "__main__":
    main()
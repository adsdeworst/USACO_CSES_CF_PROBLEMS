import sys

def main():
    [n, t] = list(map(int, sys.stdin.readline().strip("\n").split()))
    song_ratings = []
    for _ in range(n):
        song_ratings.append(int(sys.stdin.readline().strip("\n")))
    for _ in range(t):
        song_num, song_ratings = make_action(song_ratings, n)
        print(song_num)


def make_action(my_list, n):
    maximum = max(my_list)
    addend = maximum//(n - 1)
    leftover = maximum%(n - 1)
    song_num = my_list.index(maximum)
    my_list[song_num] = 0
    for i in range(n):
        if i != song_num:
            my_list[i] += addend
            if leftover > 0:
                my_list[i] += 1
                leftover -= 1
    
    return song_num + 1, my_list

main()